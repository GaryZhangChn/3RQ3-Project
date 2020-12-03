from location import Location
from user import User
from image import Image

def test_location():
    user1 = User('abc123','user1')
    image1 = Image('000001','none','none','none')
    image1.user = user1
    user1gps = Location('43.2588304,-79.9149844', 'Canada', 'Hamilton')
    user2gps = Location('40.6775666,-74.1353334', 'United States', 'New York')
    if user1.priv == True:
        image1.city = user1gps.city
    assert image1.city == 'Hamilton', "The image1.city should be user1 location"
 #   assert image1.city == 'New york', "This image should not have user2 location"
