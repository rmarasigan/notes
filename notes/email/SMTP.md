# SMTP (Simple Mail Transfer Protocol)

It is an application that is used to send, receive, and relay outgoing emails between senders and receivers. When an email is sent, it’s *transferred over the internet from one server to another using SMTP*. In simple terms, an SMTP email is just an email sent using the SMTP server.

If the SMTP server is used to send emails, then we can define SMTP relay as a process of transferring an email from one server to another. *It is mainly used to deliver emails from one domain to another domain, which is different from the user’s domain.* The **SMTP relay service** can be used to resolve a lot of issues such as email deliverability, IP blacklisting, and so on.

## Overview of SMTP Commands
The SMTP server understands simple text commands. The most common commands are as follows:

* **HELO**
  - Introduce yourself
  - “Hello.”– the client logs on with its computer name and starts the session

* **EHLO**
  - Introduce yourself and request extended mode

* **MAIL FROM**
  - Specify the sender
  - The client names the sender of the e-mail

* **RCPT TO**
  - Specify the recipient
  - “Recipient” – the client names the recipient of the e-mail

* **DATA**
  - Specify the body of the email
  - The client initiates the transmission of the e-mail

* **RSET**
  - The client terminates the initiated transmission, but maintains the connection between client and server

* **VRFY/EXPN**
  - “Verify”/“Expand”– the client checks whether a mailbox is available for message transmission

## Overview of server status codes

Informative Status Code

STATUS CODE        | PLAIN TEXT MESSAGE                                                        |
------------------ | ------------------------------------------------------------------------- |
101                | Unable to connect to server                                               |
111                | Connection refused                                                        |

Success Status Code : whenever a positive delivery code is returned from DSN

STATUS CODE        | PLAIN TEXT MESSAGE                                                        |
------------------ | ------------------------------------------------------------------------- |
200                | (Non-standard success); System status message                             |
211                | System status or system help reply                                        |
214                | A response to the HELP command                                            |
220                | Server ready for SMTP session                                             |
221                | Server ends the connection                                                |
250                | Requested mail action OK, completed                                       |
251                | User not local; mail is forwarded                                         |
252                | Cannot verify (VRFY) user, but will accept message and attempt delivery   |
253                | Pending messages for node started                                         |

Redirection Status Code

STATUS CODE        | PLAIN TEXT MESSAGE                                                   |
------------------ | -------------------------------------------------------------------- |
354                | Server starts mail input                                             |

Persistent transient failure Status Code

STATUS CODE        | PLAIN TEXT MESSAGE                                                                                    |
------------------ | ----------------------------------------------------------------------------------------------------- |
420                | Timeout connection problem                                                                            |
421                | Server not available, connection is terminated                                                        |
422                | The recipient’s mailbox has exceeded its storage limit                                                |
431                | Not enough space on the disk                                                                          |
432                | Recipient’s incoming mail queue has been stopped                                                      |
441                | The recipient’s server is not responding                                                              |
442                | The connection was dropped during the transmission                                                    |
446                | The maximum hop count was exceeded for the message                                                    |
447                | Message timed out because of issues concerning the incoming server                                    |
449                | Routing error                                                                                         |
450                | Command not executed, mailbox unavailable                                                             |
451                | Requested action aborted: local error in processing                                                   |
452                | Requested action not taken: insufficient system storage; Too many emails sent or too many recipients  |
471                | RAn error of your mail server                                                                         |

Server Permanent Error Codes

STATUS CODE        | PLAIN TEXT MESSAGE                                                  |
------------------ | ------------------------------------------------------------------- |
500                | Syntax error, command unrecognized                                  |
501                | Syntax error in parameters or arguments                             |
502                | Command not implemented                                             |
503                | Bad sequence of commands, or requires authentication                |
504                | Command parameter not implemented                                   |
510 / 511          | Bad email address                                                   |
512                | Host server for the recipient’s domain name cannot be found in DNS  |
513                | Address type is incorrect                                           |
523                | Size of your mail exceeds the server limits                         |
521                | Server doesn’t accept any mails                                     |
530                | Access denied; authentication required                              |
541                | The recipient address rejected your message                         |
550                | Requested action not taken: mailbox unavailable                     |
551                | User not local; please try forward path                             |
552                | Requested mail action aborted: exceeded storage allocation          |
553                | Requested action not taken: mailbox name not allowed                |
554                | Transaction failed                                                  |

## Reference

* [SMTP Email](https://www.duocircle.com/content/smtp-email/smtp-server-example)
* [What is SMTP?](https://www.ionos.com/digitalguide/e-mail/technical-matters/smtp/)
* [SMTP Error Codes](https://netcorecloud.com/tutorials/smtp-code-library/)

<br />

## Tools

* [MX Toolbox](https://mxtoolbox.com/SuperTool.aspx)
* [Email Verifier](https://tools.emailhippo.com/)
* [Email Checker](https://email-checker.net/)