# Sequential UUIDs

[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

This project is a Python port of [https://github.com/tvondra/sequential-uuids](https://github.com/tvondra/sequential-uuids). For more information read [this post](https://www.2ndquadrant.com/en/blog/sequential-uuid-generators/).

## Installation

```bash
    pip install sequential-uuids
```

_Python 2 is not supported._

## Usage

```python
    >>> from sequential_uuids.generators import uuid_time_nextval
    >>> uuid_time_nextval()
    UUID('13fb3a33-d41f-43b8-ac7d-4147acd68a4e')
```

## LICENSE

MIT License

Copyright (c) 2020 Moeen Zamani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
