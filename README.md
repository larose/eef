Edit Encrypted Files
====================

Edit Encrypted Files (eef) is a command-line tool to edit encrypted
files with GPG using symmetric-key encryption.


# Quick start

Install eef from PyPI:

`$ pip install eef`

Edit an encrypted file with nano:

`$ eef notes.gpg`

Edit an encrypted file with another text editor:

`$ eef -e vi notes.gpg`


# FAQ


## How do I create a new encrypted file?

`$ eef newfile.gpg`

eef will detect that the file doesn't exist, ask the passphrase twice
and make sure they match.


## How do I show the decrypted file without eef?

With `less`:

```
$ less notes.gpg
Enter passphrase:
...
```

Note: `less` only asks the passphrase for files ending with `.gpg`.


## How does eef work?

eef:

- decrypts the file and stores it under the `/dev/shm` directory;
- starts the text editor;
- encrypts the file back;
- shreds and removes the decrypted file.


## Why does eef not use the `$EDITOR` environment variable?

Because `$EDITOR` might create backup files of the decrypted
file. That is why eef uses `nano --ignorercfiles` by default.


# Author

Mathieu Larose <mathieu@mathieularose.com>


# License

eef is released under the GPLv3. See the LICENSE file for details.


# Website

http://github.com/larose/eef
