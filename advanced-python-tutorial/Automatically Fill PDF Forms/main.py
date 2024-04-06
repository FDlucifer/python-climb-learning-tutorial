# pip install fillpdf
import datetime
from fillpdf import fillpdfs

form_fields = fillpdfs.get_form_fields('template.pdf')

customer_id = 'ID1'
address = 'My Street 20'
price = '500'
date = datetime.datetime.today()
accept = 'casdcafbsdfvsdf'

data_dict = {
    form_fields[0]: customer_id,
    form_fields[1]: address,
    form_fields[2]: price,
    form_fields[3]: date,
    form_fields[4]: 'yes_xcky'
}

fillpdfs.write_fillable_pdf('template.pdf', 'new.pdf', data_dict)
