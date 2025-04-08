#import user_profile
#from user_profile import build_profile
#from user_profile import build_profile as bp
#import user_profile as up
from user_profile import *

user_profile = build_profile('albert', 'einstein', location = 'princeton', field='physics')
print(user_profile)