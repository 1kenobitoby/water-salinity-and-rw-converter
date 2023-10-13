import streamlit as st
import math

st.set_page_config(
    page_title="Water salinity and Rw converter",
    page_icon="media/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27"
    #}
)

# hack function to make only one of the module selector checkboxes selectable at a time
def disable_other_checkboxes(*other_checkbox_keys):
    for checkbox_key in other_checkbox_keys:
        st.session_state[checkbox_key] = False    

# html strings used to render donate button and link and text
donate_text = '<h6> Useful? Buy us a coffee. </h6>'

html_donate_button = '''
<form action="https://www.paypal.com/donate" method="post" target="_blank">
<input type="hidden" name="hosted_button_id" value="6X8E9CL75SRC2" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button"/>
<img alt="" border="0" src="https://www.paypal.com/en_GB/i/scr/pixel.gif" width="1" height="1" />
</form>
'''   

def redirect_button(url: str):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div>
        <img src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" alt="Donate with PayPal button">
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

st.image('media/logo.png', width=100)
st.title('Water salinity and Rw converter')

st.write('This app performs conversions between water salinity (in NaCl ppm equivalent) and formation water resistivity (Rw). It has different modes depending on your use case. Its main function is for petrophysical interpretation of wireline logs, especially water saturation calculations. Expand the \'Notes\' section at the bottom for a full explanation.')

temp_units = st.radio('Select your temperature units',
    ('Celsius', 'Fahrenheit')
)

st.write('\n')
st.write('And what do you want to calculate?')
calc_rw=st.checkbox(
    'I know salinity in ppm NaCl and I want to calculate Rw at a given temperature',
    key = "op1",
    # call disable_other_checkboxes function and pass other checkbox keys as arguments to be set to False
    on_change = disable_other_checkboxes,
    args = ("op2", "op3"),
    )
temp_conv = st.checkbox(
    'I know Rw at one temperature and I want to calculate it at a different temperature',
    key = "op2",
    on_change = disable_other_checkboxes,
    args = ("op1", "op3"),
    )
calc_salinity = st.checkbox(
    'I know Rw at a given temperature and I want to know what salinity (ppm NaCl) that equates to',
    key = "op3",
    on_change = disable_other_checkboxes,
    args = ("op1", "op2"),
    )


if calc_rw:
    water_sal = st.number_input('Enter your water salinity in ppm NaCl', min_value=0, max_value=260000, help="Type a number, no commas or full stops, hit 'Enter'")
    if water_sal:
        column1, column2 = st.columns([1.6, 0.4])
        with column1:
            if temp_units == 'Celsius':
                target_temp = st.slider('Water temperature to calculate Rw for', min_value=10, max_value=260, value=24, step = 1)
            else:    
                target_temp = st.slider('Water temperature to calculate Rw for', min_value=50, max_value=500, value=75, step = 1)

        with column2:
            st.write('\n')
            st.write('\n')
            st.write('\n')
            st.write(u'\u2070', temp_units)

        if target_temp:
            Rw75 = 0.0123+(3657.5/(water_sal**0.955)) 
            # Convert to target temperature
            if temp_units == 'Celsius':
                RwTarget = Rw75*((23.89+21.5)/(target_temp+21.5))
            else:
                RwTarget = Rw75*((75+6.77)/(target_temp+6.77))
            str_target_temp = str(target_temp)
            st.header(' ')
            output_string = '<h3>At ' + str_target_temp + u'\u2070' + temp_units[:1] + ' your Rw is' + '<span style="color:#F63366;"> ' + "%.3f" % RwTarget + ' &Omega;m</span></h3>'
            st.markdown(output_string, unsafe_allow_html=True)
            st.write('\n')
            left, right = st.columns([1, 3])
            with left:
                st.write('\n')
                st.markdown(donate_text, unsafe_allow_html=True)

            with right:
                st.write('\n')
                redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2")
              

elif temp_conv:
    known_rw = st.number_input('What is the known Rw value (&Omega;m)?', min_value=0.0, max_value=20.0, format="%.3f", step=0.001,)
    if known_rw:
        column1, column2 = st.columns([1.6, 0.4])
        with column1:
            known_temp = st.number_input('And what temperature is that Rw measured at?', min_value=0, max_value=500, step=1)

        with column2:
            st.write('\n')
            st.write('\n')
            st.write('\n')
            st.write(u'\u2070', temp_units)
    if known_rw and known_temp:
        column1, column2 = st.columns([1.6, 0.4])
        with column1:
            if temp_units == 'Celsius':
                desired_temp = st.slider('Water temperature to calculate Rw for', min_value=10, max_value=260, value=24, step = 1)
            else:    
                desired_temp = st.slider('Water temperature to calculate Rw for', min_value=50, max_value=500, value=75, step = 1)

        with column2:
            st.write('\n')
            st.write('\n')
            st.write('\n')
            st.write(u'\u2070', temp_units)

        if desired_temp:
            if temp_units == 'Celsius':
                calculated_rw = known_rw*(known_temp+21.5)/(desired_temp+21.5)
            else:
                calculated_rw = known_rw*(known_temp+6.77)/(desired_temp+6.77)    
            str_desired_temp = str(desired_temp)
            st.header(' ')
            output_string = '<h3>At ' + str_desired_temp + u'\u2070' + temp_units[:1] + ' your Rw is' + '<span style="color:#F63366;"> ' + "%.3f" % calculated_rw + ' &Omega;m</span></h3>'
            st.markdown(output_string, unsafe_allow_html=True)   
            st.write('\n')
            left, right = st.columns([1, 3])
            with left:
                st.write('\n')
                st.markdown(donate_text, unsafe_allow_html=True)

            with right:
                st.write('\n')
                redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2") 


elif calc_salinity:
    known_rw = st.number_input('What is the known Rw value (&Omega;m)?', min_value=0.0, max_value=20.0, format="%.3f", step=0.001,)
    if known_rw:
        column1, column2 = st.columns([1.6, 0.4])
        with column1:
            known_temp = st.number_input('And what temperature is that Rw measured at?', min_value=0, max_value=500, step=1)

        with column2:
            st.write('\n')
            st.write('\n')
            st.write('\n')
            st.write(u'\u2070', temp_units)

        if known_rw and known_temp:
            # Convert to equivalent Rw at 75degF
            if temp_units == 'Celsius':
                Rw75 =  known_rw*(known_temp+21.5)/(23.89+21.5)
            else:
                Rw75 = known_rw*(known_temp+6.77)/(75+6.77)    
            # Convert to salinity
            calculated_salinity = 10**((3.562-math.log10(Rw75-0.0123))/0.955)
            st.header(' ')
            if calculated_salinity <0 or calculated_salinity >300000:
                output_string = '<h3>Uhh ohh! Your calculated salinity is' + '<span style="color:#F63366;"> ' + "%.0f" % calculated_salinity + 'ppm </span> but this doesn\'t look right (expected range zero to c. 260,000ppm). Check your inputs. </h3>'

            else:
                output_string = '<h3>Your calculated salinity is' + '<span style="color:#F63366;"> ' + "%.0f" % calculated_salinity + 'ppm </span></h3>'
            st.markdown(output_string, unsafe_allow_html=True)
            st.write('\n')
            left, right = st.columns([1, 3])
            with left:
                st.write('\n')
                st.markdown(donate_text, unsafe_allow_html=True)

            with right:
                st.write('\n')
                redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2")

else:
    st.write('\n')     

st.write('\n')
st.write('\n')

notes = st.button('Notes')

notes_container1 = st.empty()
notes_image = st.empty()
notes_container2 = st.empty()
if notes:
    notes_container1.write('This app implements the Baker petrophysical log interpretation chart 2-5 Resistivity of Equivalent NaCl Solutions (see below). It is computationally almost identical to the graphical Schlumberger equivalent chart Gen-9 Resistivity of NaCl Solutions. It calculates water resistivity (Rw) for given concentrations of dissolved NaCl salt salinity and temperature or water salinity given Rw and temperature. You can also use it to convert Rw at one temperature (e.g. a lab analysis) to another temperature (e.g. your reservoir temperature).')
    notes_image.image('media/Baker_salinity.jpg', use_column_width = True)
    notes_container2.markdown('Pure water doesn\'t conduct electricity well. Electrical conductivity and resistivity are the opposites of each other so as pure water has very low electrical conductivity, it has a very high resistivity. Once one starts to dissolve salt (NaCl) in it, the Na\u207A and Cl\u207B ions are able to act as charge carriers and so salty water conducts electricity. The saltier it gets, the better it conducts and so the saltier water gets, the more its resistivity goes down. Hot water also conducts electricity better than cold water (because the ions have more energy to move and carry charge) so water resistivity goes down with temperature. Those two effects are what the chart and this app are calculating. Water becomes saturated with salt at about 260,000ppm NaCl. Na\u207A and Cl\u207B ions are by far the most abundant ions in groundwater but other ions (e.g. Mg\u00B2\u207A, Ca\u00B2\u207A, SO\u2084\u00B2\u207B) are also commonly present in groundwaters and also act as charge carriers. If you have a water analysis listing the concentrations of all these, you first need to convert the water analysis into an equivalent NaCl concentration to use the above chart (and this app). Finally while we are confident that this app is correctly implementing the above computations correctly we have no control over the ability of the end user to operate it or correctly interpret and apply the results. In other words, don\'t try and blame us because the prospect you gave a 100% COS to just came in dry.<br><small>*Comments, queries or suggestions? [Contact us](https://www.elephant-stone.com/contact.html)*.</small>', unsafe_allow_html=True)
    # Handily, there\'s another app you can use to do this (XXXX). 
    hide =st.button('Hide notes')
    if hide:
        notes = not notes
        notes_container1 = st.empty()
        notes_container2 = st.empty()
     