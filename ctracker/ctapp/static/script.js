$(document).ready(()=>{
    //functions
    var feedback=(color,result,x,y)=>{
        $('#result').css('color',color);
        $('#result').text(result);
        $('#feedback').text(x);
        $('#feedback').css('color',color);
        let z = 21.7*y; 
        $('#result1').text(z.toFixed(1));
    }
    //onclick functions
    $('#bmi').click(()=>{
        let height = $('#height').val();
        let weight = $('#weight').val();
        let metre = height/100; 
        // bmi calculations
        let m2 = metre*metre;
        let bmi = weight/m2;
        let rbmi = bmi.toFixed(1);

        //convert kg to lbs and round it off then pass it to form id 'xx'
        let res1  = $('#result1').text()*2.205;
        let qw = parseInt(res1);
        let lbs1 = qw/10;
        let lbs2= Math.ceil(lbs1);
        let lbs = lbs2*10;
        $('#xx').val(lbs);
        
        // to return bmi,result,feedback
        if(height.value==""||weight.value==""){
            feedback('black',"NaN",'Invalid',m2)
        }
        else{
            if(rbmi<18.5){
                feedback('orange',rbmi,'Underweight',m2)
            }else if(rbmi>=18.5&&rbmi<=24.9){   
                feedback('green',rbmi,'Normal',m2)                
            }else if(rbmi>=25&&rbmi<=29.9){
                feedback('red',rbmi,'Overweight',m2)
            }else if(bmi>30){
                feedback('darkred',rbmi,'Obese',m2)
            }else{
                feedback('black',"NaN",'Invalid',m2)
            }
        }
    }); 
    let pro = ()=>{//progress bar code
        let a =$('#reqcal').text();
        let b =$('#caltot').text();
        let c = b/a;
        let d = c*100;
        if(d<=100){
        $('#progress2').css({"width":d+"%",'transition': 'width 1s'});
        }
        else{
            $('#progress2').css({"width":d+"%",'transition': 'width 1s','background-color':'red'});
        }
        //if else for number spaning to the right.
        (b>100)?
        $('#num').text(b):false;
        
        //pie chart diagram code
        anychart.onDocumentReady(()=> {
            // let cal =$('#caltot').text();
            let pro =$('#protot').text();
            let fat =$('#fattot').text();
            let carbs =$('#carbstot').text();
            var data = [
                {x: "Carbs", value:carbs},
                {x: "Protein", value:pro},
                {x: "Fat", value:fat},
            ];
            var chart = anychart.pie();
            chart.title("Nutrition");
            chart.data(data);
            chart.container('piechart');
            chart.draw();
        });

    }
    // calling progress bar and pie chart code.
    pro();

});
