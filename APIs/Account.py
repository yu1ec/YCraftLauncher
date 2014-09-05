'''
Created on 2014年9月5日

@author: EcareYu

wiki:http://wiki.vg/Authentication#Authenticate
'''

'''
Authenticates a user using his password.

Payload:
{
  "agent": {                             // defaults to Minecraft
    "name": "Minecraft",                 // For Mojang's other game Scrolls, "Scrolls" should be used
    "version": 1                         // This number might be increased
                                         // by the vanilla client in the future
  },
  "username": "mojang account name",     // Can be an email address or player name for
                                         // unmigrated accounts
  "password": "mojang account password",
  "clientToken": "client identifier"     // optional
}

Response
{
  "accessToken": "random access token",  // hexadecimal
  "clientToken": "client identifier",    // identical to the one received
  "availableProfiles": [                 // only present if the agent field was received
    {
      "id": "profile identifier",        // hexadecimal
      "name": "player name",
      "legacy": true or false          // In practice, this field only appears in the response if true.  Default to false.
    }
  ],
  "selectedProfile": {                   // only present if the agent field was received
    "id": "profile identifier",
    "name": "player name",
    "legacy": true or false
  }
}
'''
authenticateUrl = 'https://authserver.mojang.com/authenticate'

'''
Refreshes a valid accessToken. It can be uses to keep a user logged in between 
gaming sessions and is preferred over storing the user's password in a file (see lastlogin).

Payload
{
  "accessToken": "valid accessToken",
  "clientToken": "client identifier"     // This needs to be identical to the one used
                                         // to obtain the accessToken in the first place
  "selectedProfile": {                   // optional; sending it will result in an error
    "id": "profile identifier",          // hexadecimal
    "name": "player name"
  }
}

Response
{
  "accessToken": "random access token",  // hexadecimal
  "clientToken": "client identifier",    // identical to the one received
  "selectedProfile": {
    "id": "profile identifier",          // hexadecimal
    "name": "player name"
  }
}
'''
refreshUrl = 'https://authserver.mojang.com/refresh'

'''
Checks if an accessToken is a valid session token with a currently-active session. 
Note: this method will not respond successfully to all currently-logged-in sessions, 
just the most recently-logged-in for each user. 
It is intended to be used by servers to validate that a user should be connecting
 (and reject users who have logged in elsewhere since starting Minecraft),
 NOT to auth that a particular session token is valid for authentication purposes. 
To authenticate a user by session token, use the refresh verb and catch resulting errors.

Payload
{
  "accessToken": "valid accessToken",
}

Response
Returns an empty payload if successful.
'''
validateUrl = 'https://authserver.mojang.com/validate'

'''
Invalidates accessTokens using an account's username and password.

Payload
{
  "username": "mojang account name",
  "password": "mojang account password",
}

Response
Returns an empty payload if successful.
'''
signoutUrl = 'https://authserver.mojang.com/signout'

'''
Invalidates accessTokens using a client/access token pair.

Payload
{
  "accessToken": "valid accessToken",
  "clientToken": "client identifier"     // This needs to be identical to the one used
                                         // to obtain the accessToken in the first place
}

Response
Returns an empty payload if successful.
'''
invalidateUrl = 'https://authserver.mojang.com/invalidate'