# BeatFinder

#### Recognize background music in YouTube clips with foreground audio overlays.

This project is part of <a href="https://cuhack.it" target="_blank">CUHackIt 2022</a>, and was produced as a collaborative effort by <a href="https://github.com/grantgonzalez14" target="_blank">Grant Gonzalez</a>, <a href="https://github.com/DineshchandarR" target="_blank">Dineshchandar Ravichandran</a>, <a href="https://github.com/sulliops" target="_blank">Owen Sullivan</a>, <a href="https://github.com/nik1097" target="_blank">Nikhil Suresh</a>, and <a href="https://github.com/zikpefu" target="_blank">Zachary Ikpefua</a>.

----

**Purpose:**

BeatFinder leverages Amazon's AWS platform (Lambda functions) and a host of open-source libraries (ffmpeg, etc.) to split audio from a selected portion of a YouTube video and identify background music using audio fingerprinting.

The project is comprised of a front-end, which parses URL input and allows users to select the start and end times for their clip, and a back-end which receives data from the user and processes audio. A haphazard mixture of home-grown scripts and publicly available functions are used to complete the analyzation, start to finish.

----

**Contributions:**

Each core function of the program and website were completed simultaneously by the various team members:

<a href="https://github.com/grantgonzalez14" target="_blank">Grant Gonzalez</a> — 

<a href="https://github.com/DineshchandarR" target="_blank">Dineshchandar Ravichandran</a> — Separation of foreground speech from background music using Python.

<a href="https://github.com/sulliops" target="_blank">Owen Sullivan</a> — Front-end in HTML, CSS, and JavaScript, as well as domain administration.

<a href="https://github.com/nik1097" target="_blank">Nikhil Suresh</a> — Separation of audio from YouTube video using Python, as well as Lambda function setup.

<a href="https://github.com/zikpefu" target="_blank">Zachary Ikpefua</a> — Audio fingerprinting and identification of background music using Python.

----

**Resources used:**

