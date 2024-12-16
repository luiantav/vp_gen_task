/* ---- TITRATION FUNCTIONS ---- */
function parse(file){
    var out = {};
    out.trial = []; //trial number
    out.rho = []; //rho target
    out.choice = []; 
    out.condition = [];
    out.task = [];
    out.iti = [];
    out.isi = [];
    out.block = [];
    out.first = [];

    var allText = vars[file];
    var line_length = allText[0].length
    var allText = vars[file] + '';
  
    String.prototype.chunkArr = function (length) {
        var data = this.split(",");
        var result = Array();
        while(data.length > 0) {
            result.push(
                data.splice(0,length)
                .join(",") 
            )}
        return result;
    }
    var lines = allText.chunkArr(line_length)
  
    lines.map(function(item){
      var tabs = item.split(','); // split lines by tabs
      out.trial.push(tabs[0]);
      out.rho.push(tabs[1]);
      out.choice.push(tabs[2]);
      out.condition.push(tabs[3]);
      out.task.push(tabs[4]);
      out.iti.push(tabs[5]);
      out.isi.push(tabs[6]);
      out.block.push(tabs[7]);
      out.first.push(tabs[8]);

    });
    return out;
  };
  
function build(sequence){ 
    var trials = []; 
    var i;
    for (i = 0; i < sequence.trial.length; i++) {

      var choice;
        if (sequence.choice[i] == '0') {
          choice = same
        } else {
        choice = different
        };

        var sameness;
        if (sequence.choice[i] == '0') {
          sameness = 'same'
        } else {
        sameness = 'different'
        };

        var task;
        if (sequence.task[i] == '1') {
          task = 'demo'
        } else {
        task = 'kaern'
        };

      var pu;
        if (sequence.condition[i] == 0) {
          pu = param.p1
        } else if (sequence.condition[i] == 1){
          pu = param.p2
        } else if (sequence.condition[i] == 2){
          pu = param.p3
        }else if (sequence.condition[i] == 3) {
          pu = param.p4
        }else if (sequence.condition[i] == 4) {
          pu = param.p5
        }else {
          pu = param.p6
        };

      var trial = {};
      trial.trial = parseFloat(sequence.trial[i]);
      trial.rho = parseFloat(sequence.rho[i]);
      trial.choice = choice;
      trial.condition = parseFloat(sequence.condition[i]);
      trial.task = task;
      trial.iti = parseFloat(sequence.iti[i]);
      trial.isi = parseFloat(sequence.isi[i]);
      trial.block = parseFloat(sequence.block[i]);
      trial.first = parseFloat(sequence.first[i]);
      trial.sameness = sameness;
      trial.pu = pu

      trials.push(trial); // add trial to timeline variable array
      };
    return trials;
  };


/* ---- LEARNING FUNCTIONS ---- */

function parseLearning(file){
  var out = {};
  out.trial = []; //trial number
  out.rho = []; //rho target
  out.condition = [];
  out.task = [];
  out.iti = [];
  out.isi = [];
  out.block = [];
  out.ouA = [];
  out.ouB = [];
  out.ouC = [];

  var allText = vars[file];
  var line_length = allText[0].length
  var allText = vars[file] + '';

  String.prototype.chunkArr = function (length) {
      var data = this.split(",");
      var result = Array();
      while(data.length > 0) {
          result.push(
              data.splice(0,length)
              .join(",") 
          )}
      return result;
  }
  var lines = allText.chunkArr(line_length)

  lines.map(function(item){
    var tabs = item.split(','); // split lines by tabs
    out.trial.push(tabs[0]);
    out.rho.push(tabs[1]);
    out.condition.push(tabs[2]);
    out.task.push(tabs[3]);
    out.iti.push(tabs[4]);
    out.isi.push(tabs[5]);
    out.block.push(tabs[6]);
    out.ouA.push(tabs[7]);
    out.ouB.push(tabs[8]);
    out.ouC.push(tabs[9]);

  });
  return out;
};

function buildLearning(sequence){ 
  var trials = []; 
  var i;
  for (i = 0; i < sequence.trial.length; i++) {

    var task;
        if (sequence.task[i] == '3') {
          task = 'learn'
        };

    var pu;
        if (sequence.condition[i] == 0) {
          pu = param.p1
        } else if (sequence.condition[i] == 1){
          pu = param.p2
        } else if (sequence.condition[i] == 2){
          pu = param.p3
        }else if (sequence.condition[i] == 3) {
          pu = param.p4
        }else if (sequence.condition[i] == 4) {
          pu = param.p5
        }else {
          pu = param.p6
        };


    var trial = {};
    trial.trial = parseFloat(sequence.trial[i]);
    trial.rho = parseFloat(sequence.rho[i]);
    trial.condition = parseFloat(sequence.condition[i]);
    trial.task = task;
    trial.iti = parseFloat(sequence.iti[i]);
    trial.isi = parseFloat(sequence.isi[i]);
    trial.block = parseFloat(sequence.block[i]);
    trial.ouA = parseFloat(sequence.ouA[i]);
    trial.ouB = parseFloat(sequence.ouB[i]);
    trial.ouC = parseFloat(sequence.ouC[i]);
    trial.pu = pu;

    trials.push(trial); // add trial to timeline variable array
    };
  return trials;
};

/* ---- GENERALISATION FUNCTIONS ---- */

function parseGeneralise(file){
  var out = {};
  out.trial = []; //trial number
  out.gen = []; //rho target
  out.condition = [];
  out.task = [];
  out.iti = [];
  out.isi = [];
  out.block = [];

  var allText = vars[file];
  var line_length = allText[0].length
  var allText = vars[file] + '';

  String.prototype.chunkArr = function (length) {
      var data = this.split(",");
      var result = Array();
      while(data.length > 0) {
          result.push(
              data.splice(0,length)
              .join(",") 
          )}
      return result;
  }
  var lines = allText.chunkArr(line_length)

  lines.map(function(item){
    var tabs = item.split(','); // split lines by tabs
    out.trial.push(tabs[0]);
    out.gen.push(tabs[1]);
    out.condition.push(tabs[2]);
    out.task.push(tabs[3]);
    out.iti.push(tabs[4]);
    out.isi.push(tabs[5]);
    out.block.push(tabs[6]);
  });
  return out;
};

function buildGeneralise(sequence){ 
  var trials = []; 
  var i;
  for (i = 0; i < sequence.trial.length; i++) {

    var task;
        if (sequence.task[i] == '4') {
          task = 'gen'
        };

    var pu;
        if (sequence.condition[i] == 0) {
          pu = param.p1
        } else if (sequence.condition[i] == 1){
          pu = param.p2
        } else if (sequence.condition[i] == 2){
          pu = param.p3
        }else if (sequence.condition[i] == 3) {
          pu = param.p4
        }else if (sequence.condition[i] == 4) {
          pu = param.p5
        }else {
          pu = param.p6
        };


    var trial = {};
    trial.trial = parseFloat(sequence.trial[i]);
    trial.gen = parseFloat(sequence.gen[i]);
    trial.condition = parseFloat(sequence.condition[i]);
    trial.task = task;
    trial.iti = parseFloat(sequence.iti[i]);
    trial.isi = parseFloat(sequence.isi[i]);
    trial.block = parseFloat(sequence.block[i]);
    trial.pu = pu

    trials.push(trial); // add trial to timeline variable array
    };
  return trials;
};

/* ---- SNAPSHOTS FUNCTIONS ---- */

function parseSnapshot(file){
  var out = {};
  out.trial = []; //trial number
  out.gen1 = []; //rho target
  out.gen2 = []; //rho target
  out.choice = [];
  out.order = [];
  out.condition = [];
  out.task = [];
  out.iti = [];
  out.isi = [];
  out.block = [];

  var allText = vars[file];
  var line_length = allText[0].length
  var allText = vars[file] + '';

  String.prototype.chunkArr = function (length) {
      var data = this.split(",");
      var result = Array();
      while(data.length > 0) {
          result.push(
              data.splice(0,length)
              .join(",") 
          )}
      return result;
  }
  var lines = allText.chunkArr(line_length)

  lines.map(function(item){
    var tabs = item.split(','); // split lines by tabs
    out.trial.push(tabs[0]);
    out.gen1.push(tabs[1]);
    out.gen2.push(tabs[2]);
    out.choice.push(tabs[3]);
    out.order.push(tabs[4]);
    out.condition.push(tabs[5]);
    out.task.push(tabs[6]);
    out.iti.push(tabs[7]);
    out.isi.push(tabs[8]);
    out.block.push(tabs[9]);
  });
  return out;
};

function buildSnapshot(sequence){ 
  var trials = []; 
  var i;
  for (i = 0; i < sequence.trial.length; i++) {

    var task;
        if (sequence.task[i] == '9') {
          task = 'snap'
        };

    var choice;
        if (sequence.choice[i] == '0') {
          choice = same
        } else {
        choice = different
        };

    var sameness;
        if (sequence.choice[i] == '0') {
          sameness = 'same'
        } else {
        sameness = 'different'
        };

    var pu;
        if (sequence.condition[i] == 0) {
          pu = param.p1
        } else if (sequence.condition[i] == 1){
          pu = param.p2
        } else if (sequence.condition[i] == 2){
          pu = param.p3
        }else if (sequence.condition[i] == 3) {
          pu = param.p4
        }else if (sequence.condition[i] == 4) {
          pu = param.p5
        }else {
          pu = param.p6
        };

    var trial = {};
    trial.trial = parseFloat(sequence.trial[i]);
    trial.gen1 = parseFloat(sequence.gen1[i]);
    trial.gen2 = parseFloat(sequence.gen2[i]);
    trial.sameness = sameness
    trial.choice = choice
    trial.order = parseFloat(sequence.order[i]);
    trial.condition = parseFloat(sequence.condition[i]);
    trial.task = task;
    trial.iti = parseFloat(sequence.iti[i]);
    trial.isi = parseFloat(sequence.isi[i]);
    trial.block = parseFloat(sequence.block[i]);
    trial.pu = pu;


    trials.push(trial); // add trial to timeline variable array
    };
  return trials;
};

/* ---- SAVING FUNCTIONS ---- */

function final_save(){
    var jsdata = jsPsych.data.get().json();
        const outdata = {partial: false, subid: "gen_sess1_" +subject_id.toString(), data: jsdata} //, structure according to ARC
        postDataSURVEY(JSON.stringify(outdata));
  }
  
  function final_save2(){
    var jsdata = jsPsych.data.get().json();
        const outdata = {partial: false, subid: "gen_sess2_" +subject_id.toString(), data: jsdata} //, structure according to ARC
        postData(JSON.stringify(outdata));
  }

  function final_save3(){
    var jsdata = jsPsych.data.get().json();
        const outdata = {partial: false, subid: "gen_sess3_" +subject_id.toString(), data: jsdata} //, structure according to ARC
        postData(JSON.stringify(outdata));
  }

  function wait(ms){
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {end = new Date().getTime(); }
  }
  
  var attempts = 0 , errorattempts = 0
  var postData = function(data){
    console.log('entered postData');
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'handle_data.php', true); // change 'write_data.php' to point to php script.
    xhr.setRequestHeader('Content-Type', 'application/json');
  
    xhr.addEventListener('readystatechange', function(e) {
          if( this.readyState === 4 ) {
            console.log(xhr.responseText)
            console.log('bye')
            //window.location.replace("http://www.thebestdinosaur.com")
            window.location.replace("https://app.prolific.co/submissions/complete?cc="+completion_code)
            //window.location.replace("https://survey.academiccloud.de/index.php/614246?lang=en&PROLIFIC_PID="+prolific_pid)

          }});
    
    //console.log(data);
    xhr.send(data);
  
  
      }

      var attempts = 0 , errorattempts = 0
      var postDataSURVEY = function(data){
        console.log('entered postData');
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'handle_data.php', true); // change 'write_data.php' to point to php script.
        xhr.setRequestHeader('Content-Type', 'application/json');
      
        xhr.addEventListener('readystatechange', function(e) {
              if( this.readyState === 4 ) {
                console.log(xhr.responseText)
                console.log('bye')
                window.location.replace("http://c101-137.cloud.gwdg.de/gen_pilot/phd_task/Titration/test.html?PROLIFIC_PID=" +prolific_pid)
                if(br.name == 'Chrome' ){window.location.replace("http://c101-137.cloud.gwdg.de/gen_pilot/phd_task/Titration/test.html?PROLIFIC_PID=" +prolific_pid)}
                else 
                //window.location.replace("http://www.thebestdinosaur.com")
                //window.location.replace("https://app.prolific.co/submissions/complete?cc="+completion_code)
                window.location.replace("https://survey.academiccloud.de/index.php/614246?lang=en&PROLIFICID="+prolific_pid)
                //window.location.replace("http://c101-137.cloud.gwdg.de/gen_pilot/phd_task/Titration/test.html?PROLIFICID="+ prolific_pid)
                
                
    
              }});
        
        //console.log(data);
        xhr.send(data);
      
      
          }

  var attempts = 0 , errorattempts = 0
  var postParam = function(data){
    console.log('entered postParameters');
    var xhr = new XMLHttpRequest();
    console.log('new xhr created')
    xhr.open('POST', 'handle_param.php', true); // change 'write_data.php' to point to php script.
    xhr.setRequestHeader('Content-Type', 'application/json');
      
    xhr.addEventListener('readystatechange', function(e) {
          if( this.readyState === 4 ) {
          console.log(xhr.responseText)
          console.log('bye')
          //window.location.replace("http://www.thebestdinosaur.com")
          //window.location.replace("https://app.prolific.co/submissions/complete?cc="+completion_code)
        }});
        
        //console.log(data);
        xhr.send(data);
    }
      

            


/* ---- GENERAL FUNCTIONS ---- */

function add(arr) {
  return arr.reduce((a,b) => a + b, 0);
}

  function shuffle(a) {
        var j, x, i;
        for (i = a.length - 1; i > 0; i--) {
            j = Math.floor(Math.random() * (i + 1));
            x = a[i];
            a[i] = a[j];
            a[j] = x;
        }
        return a;
    }


  function range(start, end) {
      return Array(end - start + 1).fill().map((_, idx) => start + idx)
    }

