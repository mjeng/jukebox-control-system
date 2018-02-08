# jukebox-control-system
I built a jukebox that could play music from a phone, or directly from music stored on the Raspberry Pi controlling the jukebox. An Arduino was also used; may be added to Git later on.
This repository includes code from the project done on the Raspberry Pi.

Full project description:

I worked as the project lead in a small team of 4 (including me) people to design a Jukebox whose function was to port the play/pause/skip/volume buttons on a phone music-control interface onto a big, communally-accessible control system. As the project lead, I designed the project and compartmentalized it into parts to assign to different team members. I also programmed the Arduino and many of the Raspberry Pi functionalities (see next section) and did the EE section of the project.

On the CS side, we worked with an Arduino (C++) to control the lights physically on the Jukebox, and we worked with a Raspberry Pi (Python) to control the music storage/feed/playback. On the Arduino we imported/worked with the FastLED library compatible with the set of LED lights we bought in order to program light patterns. On the Raspberry Pi, we implemented a few key functionalities:

(1) Users could directly upload music onto the Jukebox and play music without any phone or wireless connection. Music was uploaded directly into a specified folder on the microSD card used by the RPi, and the Jukebox could shuffle and draw music files from this folder to play (using the built-in OMXPlayer on the microcontroller).
(2) Users could connect their phone to the Jukebox through bluetooth, which we implemented using the BlueZ library.
(3) Users could connect their phone using AUX. More on this in the EE section:

On the EE side, we connected the Raspberry Pi GPIO pins into a breadboard that also connected to the buttons on the outside of the Jukebox. Each button would close a circuit, sending a signal to a corresponding GPIO pin, after which would be processed by our RPi software to either play/pause/skip/change volume.

Regarding functionality (3), we didn't find a way to send signals to the phone directly through an auxiliary cable to the phone, so we instead stripped a pair of Apple headphones and took their music-control circuit board and soldered it into our own circuit.
