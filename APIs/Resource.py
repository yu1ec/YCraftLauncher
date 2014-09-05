'''
Created on 2014年9月5日

@author: EcareYu
'''

'''
Check  the status of all Minecraft  server
wiki:https://github.com/tomsik68/mclauncher-api/wiki/Mojang-Services-Status
'''
checkUrl = 'http://status.mojang.com/check'

'''
All versions of Minecraft info
wiki:https://github.com/tomsik68/mclauncher-api/wiki/s3.amazonaws.com-Minecraft.Download
'''
versionsUrl = 'http://s3.amazonaws.com/Minecraft.Download/versions/versions.json' 

'''
NOTE:MAY BE NEED VPN
e.g https://s3.amazonaws.com/Minecraft.Download/indexes/1.8.json
wiki:https://github.com/tomsik68/mclauncher-api/wiki/Minecraft-1.6-resources
'''
indexesUrl = 'https://s3.amazonaws.com/Minecraft.Download/indexes/%s.json'

'''
Single version of Minecraft inof
e.g http://s3.amazonaws.com/Minecraft.Download/versions/1.7.3/1.7.3.json
wiki:https://github.com/tomsik68/mclauncher-api/wiki/Extended-version-information
'''
versionJsonUrl = 'http://s3.amazonaws.com/Minecraft.Download/versions/%s/%s.json'

'''
wiki:https://github.com/tomsik68/mclauncher-api/wiki/Libraries
'''
librariesUrl = 'https://libraries.minecraft.net/'