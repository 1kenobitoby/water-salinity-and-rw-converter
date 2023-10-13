# Water salinity and Rw converter
A web app that allows the user to convert formation water salinities to equivalent water resistivities (Rw) at a given temperature or vice versa. Also allows the user to convert Rw measured at one temperature to Rw at a different temperature.

# Project description
This is a Streamlit web app written in Python 3.8.10. It implements the equations which govern a graphical method of water salinity based calculations widely used mainly in the oil industry for petrophysical interpretation of wireline logs.<br>
The app has three user modes: conversion of a known water salinity to an equivalent water resistivity at a given temperature; conversion of a measured Rw value at a given temperature into an equivalent formation water salinity in ppm NaCl equivalent; and conversion of an Rw known at one temperature into Rw at a different temperature.<br> These are functions used widely in the determination of subsurface water saturation. They are traditionally determined laboriously by graphical methods or are commonly implemented in large integrated petrophysical software packages. The disadvantage of using the latter method is that the packages are expensive so commonly few (if any) licences are available. Hogging a licence for routine calculations is wasteful and opening and closing the packages constantly is time consuming. This app strips these functions out as a standalone freeby. You\'re welcome. Don\'t forget to say thank you with a donation.<br>
The project has been built in Streamlit V1.27 and distributed as a public app on the Streamlit Community Cloud.<br>
There are no plans to develop or update the app (except for bug fixes). Users have the option to contact the authors to suggest changes or improvements which we might implement if we think they are a good idea and it\'s worth our while. But probably not unless they also get their cheque books out.<br>

# How to run the project
Open the URL [https://water-salinity-and-rw-converter.streamlit.app](https://water-salinity-and-rw-converter.streamlit.app)

# Dependencies
streamlit (built using V1.26.0)<br>

# Licence
The code is copyrighted and no specific licence for its use or distribution is granted. That said, users are welcome to inspect the code, clone the repository and copy code snippets if doing so would help them solve problems with their own projects. But don\'t rip it off wholesale.

