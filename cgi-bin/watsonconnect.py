import simplejson as json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

def watsoncon(inptext):
    personality_insights = PersonalityInsightsV3(
      version='2016-10-20',
      username='c6617d96-f57c-4cdb-9c48-c61a0e661296',
      password='UXyzLTCuwC2b'
      )
    inptext= {
   "contentItems": [
      {
         "content": inptext,
         "contenttype": "text/plain",
         "created": 1447639154000,
         "id": "666073008692314113",
         "language": "en"
      }
   ]
}

    #with open(join(dirname(__file__), 'profile1.json')) as profile_json:
    profile = personality_insights.profile(inptext, content_type='application/json',raw_scores=True, consumption_preferences=True)

    #print(json.dumps(profile, indent=2))
    return json.dumps(profile, indent=2)