# Resource
So guys, have some time reading these stuff(s):

  * JSON Web Token -- https://jwt.io/
  * jwcrypto (I think I might use this one... probably) -- https://jwcrypto.readthedocs.io/en/latest/jwt.html

### Why jwcrypto
If you'l visit https://jwt.io, this library completes the implementation of jwt.
So far, there were no known security vulnerability report for this library, so I
think, using this library is kind of safe... Probably.

Like I said to you, I consider implementing my own jwt. I might do that, if the
docs is lengthy. And I haven't visited the rtd page of jwcrypto atm. Will read it
later...

### And yeah.
One turn off for using external jwt library is security vuln issues. There was one
known incident before in JWT that makes it possible for attacker to do anything, I
think it was discovered around 2015:

https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/,

Libraries as of now are fixed, and I haven't heared any major vuln issue. I think
external libraries for jwt now are safe to use.....

### My opinion
JWT is not really hard to implement. I implemented my own jwt way way back before
on some of my project. The implementation is just tailored for my needs. I didn't
implement excessive functionalities tho. I just implement what I need, and I've
written it mindfully, ensuring security, and applying the core heart of why JWT
is created by community of engineers.
