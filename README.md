# FastXcodeFile
A Python script to create new files in Xcode faster.

## Motivation
I've always found creating files in Xcode incredibly annoying. It's super slow and cumbersome. Not that creating files is the bottleneck of any iOS project whatsoever, but I'd very thankful if Apple provided a way to create files in a faster and less intrusive way. This simple script aims at fixing that.

## Usage
You must first install [mod-pbxproj](https://github.com/kronenthaler/mod-pbxproj)

```
sudo pip install mod_pbxproj
```

Then, just make the appropriate changes in the script to match your Xcode project and invoke the script with the class name argument you wish. The fastest way I've found to invoke the script is via Alfred as you can see in the following gif, but you can also use some other tools like Keyboard Maestro to achieve so.

![gif](https://raw.githubusercontent.com/luisrecuenco/FastXcodeFile/master/FastXcodeFileDemoGif.gif)

## Contact
FastXcodeFile was created by Luis Recuenco: [@luisrecuenco](https://twitter.com/luisrecuenco).
