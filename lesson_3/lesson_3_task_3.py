from address import Address
from mailing import Mailing
address_1=Address("624587", "Ачит", "Красных партизан", "44/2", "25")
address_2=Address("620000", "Екатеринбург", "Ленина", "35", "5")
cost_1=120
track_1="TR-2403"
my_mailing = Mailing(to_address=address_1, from_address=address_2, cost=cost_1, track=track_1)
print(my_mailing)
