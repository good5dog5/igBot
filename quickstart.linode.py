# imports
from instapy import InstaPy
from instapy import smart_run
import random


# login credentials

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
insta_username=''
insta_password=''
session = InstaPy(username=insta_username,
                  password=insta_password,
                  multi_logs=True,
                  headless_browser=False)

follow_list = None
black_list = None

with open('username', 'r') as f:
    follow_list = f.read().splitlines()

# with open('blacklist', 'r') as f:
#     black_list = f.read().splitlines()

print(f'orig follow_list size: {len(follow_list)}')
print(f'black_list size: {len(black_list)}')

follow_list = list(set(follow_list) - set(black_list))
print(f'follow_list with black_list removed size: {len(follow_list)}')

random.shuffle(follow_list)
with smart_run(session):
  # session.set_relationship_bounds(enabled=True,
  #                                 potency_ratio=0.5,
  #                                 delimit_by_numbers=True,
  #                                 max_followers=2100,
  #                                 min_followers=30,
  #                                 min_following=10,)
  # session.set_do_follow(enabled=True, percentage=10, times=2)
  # session.set_dont_like(['nsfw', 'kia', 'ford'])
  # session.like_by_tags(["bmw", "benz", "17", "主播"], amount=10)
  #
  # session.set_do_comment(enabled=True, percentage=25)
  #
  #use a desired occurrence percentage
  session.set_simulation(enabled=True, percentage=89)
  session.set_skip_users(skip_private=False,
          private_percentage=30,
          skip_no_profile_pic=True,
          no_profile_pic_percentage=100,
          skip_business=False,
          skip_non_business=False,
          business_percentage=10)

  session.set_quota_supervisor(enabled=True,
          sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
          sleepyhead=True,
          stochastic_flow=True,
          notify_me=True,
          peak_likes_hourly=21,
          peak_likes_daily=57,
          peak_comments_hourly=6,
          peak_comments_daily=20,
          peak_follows_hourly=20,
          peak_follows_daily=100,
          peak_unfollows_hourly=10,
          peak_unfollows_daily=42,
          peak_server_calls_hourly=287,
          peak_server_calls_daily=2410)

  session.set_action_delays(enabled=True,
          like=35,
          comment=27,
          follow=127.17,
          unfollow=28,
          story=10)

  session.unfollow_users(amount=200, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
  session.follow_by_list(follow_list, times=1, sleep_delay=542, interact=False)
  session.set_do_like(enabled=True, percentage=70)
  session.set_comments([u'酷東西', u'Really Cool', u'WoW🔥'])
  # session.follow_user_followers(follow_list,  amount=20, randomize=False)
  # session.follow_user_following(follow_list,  amount=20, randomize=False)
  session.follow_likers(follow_list, photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=True)    
  session.end()


  
