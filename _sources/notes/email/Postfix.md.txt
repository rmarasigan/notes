# Postfix

Postfix free open-source mail transfer agent that routes and delivers electronic mail. Postfix is a *Mail Transfer Agent (MTA)*: software that mail servers use to route email. Postfix is highly respected by experts for its secure design and tremendous reliability. And new users like it because it's so simple to configure. In fact, Postfix has been adopted as the default MTA on Mac OS X. It is also compatible with sendmail, so that existing scripts and programs continue to work seamlesslyafter it is installed.

### List All Emails

```bash
dev@dev: mailq
```

```bash
dev@dev: postqueue -p
```

### Flush All Emails

Delete or flush all emails from Postfix mail queue

```bash
dev@dev: postsuper -d ALL
```

### Flush Deferred Mails Only

You can only delete all deferred emails only from the mail queue. Use the following command to delete deferred emails from the queue.

```bash
dev@dev: postsuper -d ALL deferred
```

### Remove Specific Email

If you want to remove any specific email. Use the following command to remove specific emails only. First search the ID of that email like below command

```bash
dev@dev: postqueue -p | grep "email@example.com"

056CB129FF0*    5513 Sun Feb 26 02:26:27  email@example.com
```

Now delete the mail from mail queue with id 056CB129FF0.

```bash
dev@dev: postsuper -d 056CB129FF0
```

### Count Postfix Mail

```bash
dev@dev: find /var/spool/postfix/deferred -type f | wc -l
dev@dev: find /var/spool/postfix/active -type f | wc -l
dev@dev: find /var/spool/postfix/bounce -type f | wc -l
dev@dev: find /var/spool/postfix/incoming -type f | wc -l
```

## Reference

* [Flush Postfix Mail Queue](https://tecadmin.net/flush-postfix-mail-queue/)
* [Postfix: The Definitive Guide](https://www.oreilly.com/library/view/postfix-the-definitive/0596002122/)
* [How To: Postfix Flush the Mail Queue Using CLI](https://www.cyberciti.biz/tips/howto-postfix-flush-mail-queue.html)