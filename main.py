from copr import v3
client = v3.client.config_from_file('./copr.conf')
pkg = v3.PackageProxy(client)
failed = []

username = 'huakim'
project = 'kde-plasma'

from datetime import date

if (date.today().weekday() == 0) :
    today_is_monday = True
    print("Today is monday")
else:
    today_is_monday = False
    print("Today is not monday")

for i in pkg.get_list(username, project, with_latest_build=True):
    if today_is_monday:
        failed.append(i['name'])
        continue
    try:
        state = i['builds']['latest']['state']
    except Exception:
        state = 'failed'
    if state in ['failed', 'canceled']:
        failed.append(i['name'])

for i in failed:
    print(fr"send {i} to build")
    pkg.build(username, project, i)
