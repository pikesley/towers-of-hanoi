[![Build Status](http://img.shields.io/travis/pikesley/towers-of-hanoi.svg?style=flat-square)](https://travis-ci.org/pikesley/towers-of-hanoi)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://pikesley.mit-license.org)

# Surely there are easier ways to do this?

Yes, there are. This is very much a Solved Problem. However, I was inspired to implement this solution after watching [3 Blue 1 Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)'s [fascinating video](https://www.youtube.com/watch?v=2SUvWfNJSsM), in which Grant relates the Towers Of Hanoi to the Rhythm Of Counting In Binary:

![Screenshot](https://i.imgur.com/mXsl57y.png)

## Running it

I guess maybe you need to use Python Virtualenvs (I'm no Python expert), and then you should be able to do

```
make
```

to run the tests, and

```
make run discs=n
```

to actually solve

Note that the output is kind of sideways - that's because console output is not the real purpose of this - if you're running this Raspberry Pi with a [Micro Dot pHAT](https://shop.pimoroni.com/products/microdot-phat) attached, then try

```
make phat
```

to watch this all play out on the pHAT
