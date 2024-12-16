

var instruction_intro = {
    type: jsPsychHtmlKeyboardResponse,
    trial_duration: 5000,
    response_ends_trial: true,
    stimulus: 'If two flowers are the same press $key1, it they are different press $key2. >>>',
    data: {
      stimulus_type: "instructions"
    },
};




var instruction_demo_cue = {
    type: jsPsychHtmlKeyboardResponse,
    trial_duration: 2000,
    response_ends_trial: true,
    stimulus: 'same = $key1, different = $key2',
    data: {
      stimulus_type: "instructions"
    },
};




var instruction_consent1 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: '<h2> Study Information and Statement of informed Consent</h2>' +
    '<h3> 1. Aim of the study </h3>' +
    'This study is a research project of the Max Planck Institute (MPI) for Human Development. The purpose of this study is to investigate the role of uncertainty in aversive learning.' +
    '<h3> 2. Procedure and content of the study </h3>' +
    'To do this, you will be asked to perform a simple task in which you will be asked to compare different shapes. The task will take approximately 60 minutes. You will be able to take a small break halfway through the task. You will be reimbursed &pound8 for your time. Additionally, there is a &pound2 bonus that depends on your performance on the task (i.e., the total reimbursement is max. &pound10). Please only participate from a laptop computer (no mobiles, no tablets) and if your screen is at least 13-inch diagonal.'+
    '<h3> 3. What will happen to the data collected? </h3>' +
    'The data collected will be used for research purposes only. The study data will be stored under an individual code number. After payment, the key linking your Prolific ID to the individual anonymised code number will be deleted. This makes it impossible to link the study data to you. The study data may be shared with cooperation partners for collaborative analysis. The study data may also be made publicly accessible via research databases or scientific publications (typically via the Internet). This makes it possible for other researchers to check or replicate the results and enhances the quality of scientific research. The study data may also be used for new re-search questions going beyond the purposes of this particular study. Study data are only transferred or made publicly accessible without Prolific IDs or any data in which persons are identifiable.'+
    '<h3> 4. Participation is voluntary </h3>' +
    'Participation in this study is voluntary. You may withdraw from the study at any time. You may also withdraw your consent to data processing and usage at any time before payment. To do so, please contact neuroexperiments@mpib-berlin.mpg.de. Please note that data collected from you can no longer be associated with you, once your Prolific ID is deleted from the study data after payment.'+
    '<h3> 5. Consent </h3>' +
    'This study takes an average of 60 minutes. You will receive a compensation of &pound8 for your time, plus a performance bonus of max  &pound2. Please understand that we can only pay the compensation if you finish the task. We will ask you to do the task using full screen mode. If you exit the full screen, this will be considered as quitting the experiment and we can unfortunately not pay you. If you don\'t consent to the conditions outlined on the last two pages, please exit the full screen now to end the experiment. Otherwise, press any key to continue to the consent page.',

    data: {
      stimulus_type: "instructions"
    },
};

var instruction_consent2 = {
    type: jsPsychHtmlButtonResponse,
    stimulus: "<p>I have read and understood the conditions.</p>" +
    "<p> I consent to participate in the study and agree to the collection, storage, and use of my data as described above.</p>",
    choices: ['Yes']}

var instruction_welcome = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'You completed all the checks and will now continue with the experiment. <br>'+
    'Please press any key to start.',
    data: {
      stimulus_type: "instructions"
    },
};


var instruction_fullscreen = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Please remember: you have to stay in fullscreen mode to be able to complete the experiment.' +
    ' Also, you have to wear headphones during the whole experiment. Do NOT adjust the volume during the entire task or you will not be able to continue. <br>' + 'Press any key to continue.',
    data: {
        stimulus_type: "instructions"
      }
    };
  


var instruction_keys1 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Whenever you see this ">>>" you can press any key to continue. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

    
var instruction_keys2 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'To control the task you will be using two buttons: \' $key1 \', \'$key2\' and the space bar. >>> ',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_keys3 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true, 
    stimulus: 'To check that it works, please press the \' $key1 \' button.',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_keys4 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'To check that it works, please press the \' $key2 \' button.',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_keys4b = {
    type: jsPsychHtmlKeyboardResponse,
    choices: " ",
    response_ends_trial: true,
    stimulus: 'To check that it works, please press the space bar',
    data: {
        stimulus_type: "instructions"
      }
    };


var instruction_keys5 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Thank you, the buttons seem to work well. <br>' + 
    'Please place your index fingers on the \'j\' and \'f\' keys. <br'+
    'Place also place your thumbs on the space bar. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_keys5b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'This study consists of two parts. There will be a break between part one and two. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

    var spacebloom_1 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'Spacebloom session 1 >>> '+
      '<br>'+
      '<br>'+
      "<img src='img/sess1.png' width='600'></img>",
      data: {
          stimulus_type: "instructions"
        }
      };

      var spacebloom_2 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'Spacebloom session 2 >>> '+
        '<br>'+
        '<br>'+
        "<img src='img/sess2.png' width='600'></img>",
        data: {
            stimulus_type: "instructions"
          }
        };

        var spacebloom_3 = {
          type: jsPsychHtmlKeyboardResponse,
          response_ends_trial: true,
          stimulus: 'Spacebloom session 3 >>> '+
          '<br>'+
          '<br>'+
          "<img src='img/sess3.png' width='600'></img>",
          data: {
              stimulus_type: "instructions"
            }
          };


var instruction_task1 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In this study you\'ll embark on a dangerous space voyage.' +
    'You will complete a series of separate missions during which you will investigate rare space flowers that grow on different planets. Each planet has an entirely different ecosystem and produces very distinct space flowers. >>>'+
    '<br>'+
    '<br>'+
    "<img src='img/planets2.png' width='400'></img>",
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task1b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'As a trained biologist, your task is to travel to each planet and learn about the different flowers. Each species has different characteristics and some are more dangerous than others. Yes, you heard correctly, the flowers are dangerous.' + '<br>'+
    'Our Bubble telescope indicates that some flowers tend to attack and bite while screaming unbearably. >>>' + '<br>'+
    "<img src='img/telescope.png' width='200'></img>",
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task2 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In this first task, mission control will train you for the future dangerous space mission to make sure that you are ready and familiar with the different flower species you can find on the different planets.' + '<br>' + 
    'Make sure to read the next section carefully.  >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task2b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'The flowers on each planet all have the same color but they all slightly differ in shape. Some flowers have more spiky petals and some have petals that are more rounded. In this next part we will show you examples of space flowers for each planet. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task2c = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'On each trial you will see a flower followed by a scrambled image. Next, you will see a second flower. After seeing both flowers, you will be asked to indicate whether the flowers were the same or different >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };

    var instruction_task2d = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'If the two flowers were the same press $same, if they were different press $different. Make sure to respond only once you are asked to. If you don\'t know the response, press what feels right. Try it! >>>', 
      data: {
          stimulus_type: "instructions"
        }
      };

    var instruction_task_repeat = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'Place your fingers on the \'f\' and \'j\' keys. If the two flowers were the same press $same, if they were different press $different. Make sure to respond only once you are asked to. If you don\'t know the response, press what feels right. >>>', 
      data: {
          stimulus_type: "instructions"
        }
      };

    var instruction_task_repeat2 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'Press any key to start. >>>', 
      data: {
          stimulus_type: "instructions"
        }
      };

var instruction_task3 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'The difference between two flowers can be very small. In order to detect it you have to pay very close attention. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task3b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'After each trial you will see a fixation cross on the center of the screen. Please focus on it while you wait for the next trial to start. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task3c = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'On some trials it might happen that you are distracted and miss a flower or that you accidentally press the wrong button.<br>'+
    'If this happens press the space bar right after your answer, to let mission control know. <br>' +
    'Only press the space bar after your answer if it is absolutely necessary.<br>' +
    'Mission control will still count your original response. By pressing the space bar however you help them to better understand your answers. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_task3d = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'You will repeat this task for every planet. Note that flowers from different planets never mix. In fact, they have entirely different genetic makeup. Even if they can sometimes look similar you shouldn\'t combine what you learn on one planet with flowers on another. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };
    


var instruction_task4 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Here are some more practice trials. <br> '+ 
    'Remember, If the flowers were the same press $key1, if they were different press $key2. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };


var instruction_task5 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Well done, you finished the practice trials and will continue with the main task.<br>'+
    'The main task consists of 6 parts. In each one you will see flowers from a different planet.' + '<br>' +
    'The goal of the task is to get as many correct answers as possible to make sure that you are well prepared for your mission. You will no longer get feedback after each trial. Instead, mission control will count all incorrect answers and give you feedback about your performance after every block of 20 trials.', 
    data: {
        stimulus_type: "instructions"
      }
    };



var instruction_task6 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In the beginning or end of each block you might have to complete an audio check.' + '<br>' +
    'If this is the case, the phrase \'audio check\' will appear on the screen. You will then immediately hear clicking sounds. After this you will be asked to report how many clicks you heard. In order to be able to respond correctly you have to wear your headphones all the time and don\'t change the volume setting.',
    data: {
        stimulus_type: "instructions"
      }
    };

    
var instruction_task7 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Get ready to continue with the main task. Make sure that your index fingers are on the \'$key1\' and  \'$key2\' buttons. <br>'+
    'Also make sure that your thumbs are on the space bar. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

var instruction_selection = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Try to do as well as you can. There is a small chance that you are not invited back to sessions two and three of this study depeding on your performance on this task. Get ready to start. >>> ', 
    data: {
        stimulus_type: "instructions"
      }
    };


var instruction_task8 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Well done, you will now continue with the next planet. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };


var instruction_task10 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Note that the color of the flowers on this planet is different. The task remains the same. Remember, you can let mission control know when you accidentally gave a wrong response or missed a shape by pressing space bar after your answer. Please only press space bar when absolutely necessary. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };





 var instruction_task11 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'You have successfully learned about the different flowers from all planets of the galaxy. Good job. Mission control has some questions for you: >>>',
        data: {
            stimulus_type: "instructions"
          }
        };



  var instruction_task12 = {
          type: jsPsychHtmlButtonResponse,
          stimulus: 'To complete the session you will have to fill out some questionnaires. Note that your answers on these questionnaires do NOT determine progression to the next session. Once you click on the button below your data will be saved and you will automatically redirectd to the questionnaire page.' +
          'Saving might take a little while. Please wait until the process is completed.',
          choices: ['Save data and take me to the questionnaires'],
          data: {
            stimulus_type: "instructions"
          }
        };
// instructions questionnaire?

var instruction_sess2_final = {
  type: jsPsychHtmlButtonResponse,
  stimulus: 'Once you click on the button below your data will be saved and you will automatically redirectd to Prolific.' +
  'Saving might take a little while. Please wait until the process is completed. ',
  choices: ['Save data and take me to Prolific'],
  data: {
    stimulus_type: "instructions"
  }
};






var inst_attention = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: 'Before starting the experiment, we will check whether you are a human, comprehend English and your understanding of the instructions with three questions.<br>' +
        'This is a step we must take to protect the data quality.<br>'+
        'Some questions are slightly tricky and require you to pay very close attention to all texts and to answer accordingly.<br>'+
        'You must answer correctly to be able to take part in the experiment.<br>' +
        'Otherwise you will be returned to Prolific and we cannot reimburse you.<br>'+
        'Press any key to continue. >>> </p>'
  }



  /* ---- Instructions session 2 ---- */


  var instr_sess2_1 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Welcome back to session two!' + '<br>'+ 'Congratulations on being selected for the spacebloom missions! >>>' ,
    data: {
        stimulus_type: "instructions"
      }
    };

    var instr_sess2_1b = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'After learning about space flowers on different planets in session one, you are now almost ready to embark on a series of dangerous missions to learn which petal characteristics for each species are dangerous. >>>',
      data: {
          stimulus_type: "instructions"
        }
      };


  
  var instr_sess2_2 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Before you can start, mission control asks you to briefly repeat the training that you already know from session one.' + '<br>' +
    'This time it will be shorter and  is just a reminder of the different space flower species on each planet.',
    data: {
        stimulus_type: "instructions"
      }
    };

    var instr_sess2_intro1 = {
      type: jsPsychHtmlKeyboardResponse,
      trial_duration: 5000,
      response_ends_trial: true,
      stimulus: 'Remember ... >>>',
      data: {
        stimulus_type: "instructions"
      },
    };


    var instruction_sess2_never1 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You will repeat this task for every planet. Note that in this session you will only train for 3 of the 6 planets you know. You will then proceed to complete the mission for this selection of planets. The remaining planets will become relevant in session 3!>>>', 
      data: {
          stimulus_type: "instructions"
        }
      };

      var instruction_sess2_never2 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'Also remember that flowers from different planets never mix. In fact, they have entirely different genetic makeup. Even if they can sometimes look similar you shouldn\'t combine what you learn on one planet with flowers on another. >>>', 
        data: {
            stimulus_type: "instructions"
          }
        };


    var instr_sess2_snap = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You already finished the training for the first planet. That was great. Before continuing with the training for the next planet, mission control has some more questions for you... >>> ',
      data: {
        stimulus_type: "instructions"
      },
    };

    var instr_sess2_snap2 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'In the next part you will see two space flowers and you are asked to report to mission control how similar you think they are. Use the slider to indicate how similar you think they are and press continue to get to the next flower pair! >>> ',
      data: {
        stimulus_type: "instructions"
      },
    };


    var instr_sess2_snap3 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You are doing well! In the next part you will again see two space flowers and you are asked to report to mission control how similar you think they are. >>> ',
      data: {
        stimulus_type: "instructions"
      },
    };



    var instr_sess2_initial = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You will again start with the task you are already very familiar with. >>> ',
      data: {
        stimulus_type: "instructions"
      },
    };

    var instr_sess2_initial2 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You are about to start training for the last planet of this session. You will again start with the task you are already very familiar with. >>> ',
      data: {
        stimulus_type: "instructions"
      },
    };



  var instr_sess2_3 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Well done, you completed the training! Mission control will now give you more information about the mysterious space flowers. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };
    

  var instr_sess2_4 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'You have to be very careful on your mission to space!' + '<br>'+
    '<br>'+
    "<img src='img/caution.png' width='100' height='100'></img>"+
    '<br>'+
    '<br>'+
    'Some space flowers are very dangerous. As you learned in session one, on each planet flowers have the same color but they come in many shapes. Some have more spiky petals while some have rounder ones.' + '<br>' +  
    'It seems to be the case that flowers of a specific shape are quite dangerous. These so-called super space flowers produce a scream when disturbed and bite the player. Space flower bites are extremely painful! >>> ',
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_5 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'These dangerous super space flowers exist on each planet and therefore come in all colors. You can only distinguish them by their unique shape! >>> ',
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_6 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Super space flowers are known to be very moody.' + '<br>' + 
    'If you come across them in a good moment they might let you pass unharmed. If you disturb them in a bad moment they will release their horrifying scream and bite you. Super space flowers on some planets are moodier than others and as a consequence they will scream and bite you more often. Some species on other planets on the other hand tend to scream and bite less frequently.' + '<br>' + '<br>' + 
    'It is very important that you learn how moody super space flowers are on different planets to be able to predict which specific flowers are dangerous for future missions  >>> ',
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_7 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'On each mission you will visit one planet. Before you land on each planet mission control will show you super space flowers from the planet you are heading to, so that you can learn about them. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_8 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'On each trial you will see a super space flower. Depending on the flower\'s mood it will scream and bite you or not.' + '<br>' +
    'It is very important that you pay attention and learn how moody super space flowers from the upcoming planet are. After some trials we will ask you to rate how likely you think it is that a super space flower from this particular planet will scream and bite you! >>>',  

    data: {
        stimulus_type: "instructions"
      }
    };
    
  

  var instr_sess2_10 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Next you will see an example for such a rating. Please select anything you want, this is just practice. 0% means that you think there is no chance that the shown super space flower will scream at you and bite you and 100% means that it\'s certain that it will. >>>' ,
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_11 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Great, remember: In this next part you will see super space flowers from the upcoming planet that either scream at you or don\'t. Your task is to observe closely and learn and respond to the ratings once you are asked to. Good luck! >>>',
    data: {
        stimulus_type: "instructions"
      }
    };

    // 12 in main script


  var instr_sess2_13 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'Well done. You did well at learning about the super space flowers of $planet1. Get ready to land on the planet. ' + '<br>'+ 
    'On the planet you will encounter many different flowers. For each flower mission control will ask you to rate how likely you think that the flower you see screams and bites you. We need this information to be able to predict danger on future missions. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };

  var instr_sess2_14 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In order to protect you from the bites and horrible screams, you will be wearing a special space suit made of compressed space dust.' +
    '<br>'+
    '<br>'+
    "<img src='img/suit.png' width='100' height='100'></img>"+
    '<br>'+
    '<br>'+
    'Since you can\'t hear the screams and feel the bites you will have to rely on what you have learned earlier. The important thing is that mission control is recording whether the flower actually screamed and tried to bite, so they can later let you know how well you did. Remember, it is important that you give very accurate ratings to mission control. >>>',
    
    data: {
        stimulus_type: "instructions"
      }
    };
    


  var instr_sess2_14b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'We are now landing on planet $planet1. Get ready to start. >>>',
    data: {
        stimulus_type: "instructions"
      }
    };


  var instr_sess2_14c = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'You are now returning to the space ship to continue to the next planet. Mission control needs you to tell them about the space flowers you just saw one last time. You will see two space flowers and will be asked to report how similar they are. You already know this task from training. Once you are done reporting you will land on the next planet! >>>',
    
    data: {
        stimulus_type: "instructions"
      }
    };

    var instr_sess2_14d = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You are now returning to the space ship. Mission control will ask you about the space flowers you just saw one last time. Get ready! >>>',
      
      data: {
          stimulus_type: "instructions"
        }
      };


// 15 in main



var instr_sess2_16 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'Well done. We are now landing on the $planet2 planet. >>>',
  data: {
      stimulus_type: "instructions"
    }
  };

// 17 in main

var instr_sess2_18 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'Good job. We are now landing on the $planet3 planet. >>>',
  data: {
      stimulus_type: "instructions"
    }
  };


// 19 in main 

var instr_sess2_20 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'Nice! Get ready to land on the $planet4 planet. >>>',
  data: {
      stimulus_type: "instructions"
    }
  };

  // 21 is in main
var instr_sess2_22 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'We are landing on the $planet5 planet now. >>>',
  data: {
      stimulus_type: "instructions"
    }
  };

  // 23 is in main
var instr_sess2_24 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'We are now landing on the $planet6 planet. >>>',
  data: {
      stimulus_type: "instructions"
    }
  };



      halfway = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'You made it halfway. Press any key to continue. >>>',
        data: {
            stimulus_type: "instructions"
          }
        };





var instr_sess2_25 = {
  type: jsPsychHtmlKeyboardResponse,
  response_ends_trial: true,
  stimulus: 'Good job. You completed the task successfully. You did very well and will now be able to go back to planet earth. >>>', 
  data: {
      stimulus_type: "instructions"
    }
  };

  var instr_sess2_25b = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In the third and last session of this study you will be completing your mission on the remaining planets. You will be sent the link for the next session on Prolific >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };


  var instr_sess2_26 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'You will now respond to some final questions before being redirected to Prolific. >>>', 
    data: {
        stimulus_type: "instructions"
      }
    };

  


    /* Instructions session 3 */

    var instr_sess3_1 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'Welcome back to session three!' + '<br>'+ 'This is the last session of this study, get ready to complete your mission! >>>' ,
      data: {
          stimulus_type: "instructions"
        }
      };


    var instr_sess3_1b = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'In this session you will visit the three planets that you haven\'t visited in the last session to complete your mission. >>>',
      data: {
          stimulus_type: "instructions"
        }
      };



      var instr_sess3_2 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'We will again start with a brief training for each planet. Similarly to the last session you will first be asked if two consecutive flowers are the same or different. After that, you will be asked to rate how similar two flowers are. You already know all this from the last session. >>>',
        data: {
            stimulus_type: "instructions"
          }
        };



      var instruction_sess2_never3 = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You will repeat this task for every planet. Note that this time you will train for the planets that you haven\'t visited in the last session. You will then proceed to complete the mission for this selection of planets. Once you visit the last planet of this session, you have completed your mission!>>>', 
      data: {
          stimulus_type: "instructions"
        }
      };


      var instr_sess3_initial = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'You will again start with the task where you have to indicate if two flowers are the same or different. >>> ',
        data: {
          stimulus_type: "instructions"
        },
      };

  
      var instr_sess3_initial2 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'You are about to start training for the last planet of this session. You will again start with the task where you have to indicate if two flowers are the same or different. >>> ',
        data: {
          stimulus_type: "instructions"
        },
      };


      var instr_sess3_3 = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'Well done, you completed the training for all 3 planets! Mission control would like to repeat what you have to know about the space flowers. Although you already know much of it, we ask you to read it carefully. >>>',
        data: {
            stimulus_type: "instructions"
          }
        };


        var instr_sess3_11 = {
          type: jsPsychHtmlKeyboardResponse,
          response_ends_trial: true,
          stimulus: 'You are ready to start. Just remember: In this next part you will see super space flowers from the upcoming planet that either scream at you or don\'t. Your task is to observe closely and learn and respond to the ratings once you are asked to. Good luck! >>>',
          data: {
              stimulus_type: "instructions"
            }
          };


      var instr_sess3_14 = {
    type: jsPsychHtmlKeyboardResponse,
    response_ends_trial: true,
    stimulus: 'In order to protect you from the bites and horrible screams, you will again be wearing a special space suit made of compressed space dust.' +
    "<img src='img/suit.png' width='100' height='100'></img>"+
    'Remember, since you can\'t hear the screams and feel the bites you will have to rely on what you have learned earlier. The important thing is that mission control is recording whether the flower actually screamed and tried to bite, so they can later let you know how well you did. Remember, it is important that you give very accurate ratings to mission control. >>>',
    
    data: {
        stimulus_type: "instructions"
      }
    };


    var instr_sess3_25b = {
      type: jsPsychHtmlKeyboardResponse,
      response_ends_trial: true,
      stimulus: 'You completed the mission successfully. Great job!  >>>', 
      data: {
          stimulus_type: "instructions"
        }
      };


      var instr_identify = {
        type: jsPsychHtmlKeyboardResponse,
        response_ends_trial: true,
        stimulus: 'Good job, mission control has one last question before you continue >>>', 
        data: {
            stimulus_type: "instructions"
          }
        };

        var instr_identify2 = {
          type: jsPsychHtmlKeyboardResponse,
          response_ends_trial: true,
          stimulus: 'Good job, mission control has one last question.>>>', 
          data: {
              stimulus_type: "instructions"
            }
          };