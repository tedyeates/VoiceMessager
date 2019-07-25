 EmojiCodeSheet
Your first stop for developing emoji keyboards for any platform, using any language.

Tags
----
  **#EmojiCodeSheet**

Logo
----
![alt tag](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/Logo.png)

**Emoji Code Sheet** is a collection of emojees in form of programming language code. Get rid of the white boxes/missing symbols characters in your app. Develop your custom emoji keyboard using Emoji Code Sheet.

Emojees are the new way of talking. They are everywhere in all the instant messengers, social media applications. Emojees provide a very cool way for communication. 

![alt tag](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/Cool.png)


Why is the need of Emoji Code Sheet?
----
Explained in detail in this [LinkedIn article](https://www.linkedin.com/pulse/emoji-code-sheet-shayan-rais?trk=prof-post)

Platform and Language
----
Whether you are on iPhone, Android, Web or any other device, gadget, anywhere and you want to implement emoji keyboard just like WhatsApp or any other app. Emoji Code Sheet is your way to go. Just copy the emoji codes of language of your choice, either the **string symbol emojees** or **codepoints**, just do some coding to display the codepoints/symbols into textbox and your done.

How to use this in your project?
----
The detail of each language (java, objective-C, php etc) is provided in [Emoji Code Sheet Wiki] (https://github.com/shanraisshan/EmojiCodeSheet/wiki)

Guide
----
Guide Document is available at [EmojiCodeSheet_Guide](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/EmojiCodeSheet_Guide.pdf)

|ECS Version #|Date|Emojis are arranged according to|
|:-:|:-:|:-|
|2|March-2017|[WhatsApp Android version 2.17.107](https://github.com/shanraisshan/EmojiCodeSheet/tree/master/!Guide/WhatsApp%20Android%202.17.107%20Screens)|
|1|June-2016|[WhatsApp Android version 2.16.139](https://github.com/shanraisshan/EmojiCodeSheet/tree/master/!Guide/WhatsApp%20Android%20v2.16.139%20Screenshots)|

Emojees are categorized into 8 different tabs (just like WhatsApp) as follows

|1|2|3|4|5|6|7|8|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
|People|Nature|Food|Activity|Travel|Objects|Symbols|Flags|

Files are named according to ECS versions

|Version #|File names|
|:-:|:-|
|2|[People2](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/android/string/People2.java), Nature2, Food2 .....|
|1|[People](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/android/string/People.java), Nature, Food .....|

Code is available in 2 different forms.

1. Codepoints
2. Strings

Each emoji is present in the form of variable, for example
![alt tag](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/Cool.png)

**Android Example**
```java
//Codepoints Example
public static final int SMILING_FACE_WITH_SUN_GLASS = 0x1f60e; //https://www.emojibase.com/emoji/1f60e/smilingfacewithsunglasses

//String Example
public static final String SMILING_FACE_WITH_SUN_GLASS = "😎"; //https://www.emojibase.com/emoji/1f60e/smilingfacewithsunglasses
```
The purpose of pasting emojibase/emojipedia link as a comment is to verify emoji properties such as,

1. Emoji Name
2. Emoji Unicode
3. Emoji Image

![alt tag](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/Guide.png)

Custom Emojees
----
Develop keyboard for your application using your own personal custom emojees

**For Example:** 👤 👁 ✌ 🚶 🏃

![alt tag](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/custom_emojis.jpg)

Sample Implementation
----

**Android:**

[![Android](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/google_play.png)](https://play.google.com/store/apps/details?id=com.emojicodesheet)

Youtube Video
----
[![Youtube](https://github.com/shanraisshan/EmojiCodeSheet/blob/master/!Guide/youtube_small.gif)](https://www.youtube.com/watch?v=8ly2qIFcw5Q)

Acknowledgement
----
**[WhatsApp](https://http://www.apkmirror.com/apk/whatsapp-inc/whatsapp/whatsapp-2-16-139-release/)**

Emojees are arranged and categorized according to the Android WhatsApp version 2.16.139

**[Emojibase](https://www.emojibase.com/)** ,
**[Emojipedia](http://emojipedia.org/)**

Emojibase and Emojipedia links are used as a comment to verify emoji properties.

Contribute
----
If there is any idea, feedback, issue you may consider worth mentioning, please feel free to open an issue or send a pull request.

License
----

```
The MIT License (MIT)

Copyright (c) 2016 Shayan Rais (http://shanraisshan.com)

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
```
