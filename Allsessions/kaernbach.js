
// KAERNBACH variables
step_decrease = 1
step_increase = 3 // assume 75 % PU to have Norbury prior!
step_min = 1
step_max = 10



// KAERNBACH 

var stimulus_compare_kaern = {
    type: jsPsychHtmlKeyboardResponse,
    trial_duration: 1000,
    response_ends_trial: true,
    choices: [same, different],
    on_start: function(stimulus_compare) {
    current_trial = jsPsych.timelineVariable('trial')
    previous_rho = jsPsych.timelineVariable('rho')
    n_spikes = chosen_conditions[jsPsych.timelineVariable("condition")]


    if(jsPsych.timelineVariable('trial') == 1 && jsPsych.timelineVariable('choice')== same){
      rho_compare = previous_rho
      console.log("first same")
      stimulus_compare.stimulus = "<img src='Shapes/shapes_png/F" + rho_compare + "_S"+n_spikes + ".png' width='200' height='200'></img>"
      stimulus_compare.data.rho = rho_compare
      stimulus_compare.data.step = param.initial_step
      stimulus_compare.data.sameness = 'same'

    } else if (jsPsych.timelineVariable('trial') == 1 && jsPsych.timelineVariable('choice')== different){
      step = param.initial_step
      rho_compare = previous_rho + step
      console.log("first different")
      stimulus_compare.stimulus = "<img src='Shapes/shapes_png/F" + rho_compare + "_S"+n_spikes + ".png' width='200' height='200'></img>"
      stimulus_compare.data.rho = rho_compare
      stimulus_compare.data.step = param.initial_step
      stimulus_compare.data.sameness = 'different'

    } else if (jsPsych.timelineVariable('choice') == same){
      last_step = jsPsych.data.get().filter({ trial_type: 'html-keyboard-response', stimulus_type: 'comparison' }).last().values()[0].step

      rho_compare = previous_rho
      console.log('same follow')
      stimulus_compare.stimulus = "<img src='Shapes/shapes_png/F" + rho_compare + "_S"+n_spikes + ".png' width='200' height='200'></img>"
      stimulus_compare.data.rho = rho_compare
      stimulus_compare.data.step = last_step
      stimulus_compare.data.sameness = 'same'

    } else {
      console.log('titrating ...') 
      lastresponse = jsPsych.data.get().filter({ trial_type: 'html-keyboard-response', stimulus_type: 'response', correct_choice: "j" }).last().values()[0]

      if (lastresponse === undefined){
        rho_compare = previous_rho + param.initial_step
        stimulus_compare.stimulus = "<img src='Shapes/shapes_png/F" + rho_compare + "_S"+n_spikes + ".png' width='200' height='200'></img>"
        stimulus_compare.data.rho = rho_compare
        stimulus_compare.data.sameness = 'different'
        stimulus_compare.data.step = param.initial_step

      } else {
        lastresponse = lastresponse.correct
        
        if (lastresponse == 1 && last_step > step_min){
        step = last_step - step_decrease
        console.log('un', step)
        } else if (lastresponse == 1 && last_step <= step_min){
        step = step_min
        console.log('doi', step)
        } else if (lastresponse == 0 && last_step <= step_max){
        step = last_step + step_increase 
        console.log( 'trei', step)
        } else {step = step_max
        console.log('cater', step)
       }

        rho_compare = previous_rho + step
        stimulus_compare.stimulus = "<img src='Shapes/shapes_png/F" + rho_compare + "_S"+n_spikes + ".png' width='200' height='200'></img>"
        stimulus_compare.data.rho = rho_compare
        stimulus_compare.data.sameness = 'different'
        stimulus_compare.data.step = step

      }
    }

    console.log('see', previous_rho, rho_compare)
    
  },
    stimulus: '',
    data: {
      rho: rho_compare,
      step: step,
      stimulus_type: 'comparison',
      titration: 'kaern',
      correct_choice: jsPsych.timelineVariable('choice'),
      trial_n: jsPsych.timelineVariable('trial'),
      condition: jsPsych.timelineVariable('condition')
    }
};


var trial_kaern = {
    timeline: [instruction_intro, stimulus_target, stimulus_scramble, stimulus_compare_kaern, response, feedback],
    timeline_variables: protocol['sub_01'] 
  }
