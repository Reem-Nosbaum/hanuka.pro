class Customer:

    def __init__(self, id, f_name, l_name, address, mobile):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.mobile = mobile

    def __repr__(self):
        return f'Person({self.id}, {self.f_name}, {self.l_name}, {self.address},' + \
               f'{self.mobile})'

    def __str__(self):
        return f'Person id: {self.id}, first name: {self.f_name}, last name: {self.l_name}, address: {self.address}, ' + \
               f'mobile: {self.mobile} '
