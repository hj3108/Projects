// var today= new Date();
// var day="";

// if(today.getDay()=== 6 || today.getDay()===0)
// {
//     day="Weekend";
//     res.render('list', {kindOfDay: day});
// }
// else
// {
//     day="Weekday";   
//     res.render('list', {kindOfDay: day});
// }

// var currentDay=today.getDay();
// if(currentDay===0)
// {
//     day="Sunday";
// }
// else if(currentDay===1)
// {
//     day="Monday";
// }
// else if(currentDay===2)
// {
//     day="Tuesday";
// }
// else if(currentDay===3)
// {
//     day="Wednesday";
// }
// else if(currentDay===4)
// {
//     day="Thursday";
// }
// else if(currentDay===5)
// {
//     day="Friday";
// }
// else if(currentDay===6)
// {
//     day="Saturday";
// }

// var options = {
//     weekday: "long",
//     day: "numeric",
//     month: "long"
// };

// var day=today.toLocaleDateString("en-US",options);









// module.exports.getDate= getDate;
// module.exports.getDay= getDay; 

// function getDate()
// {
//     var today= new Date();
//     var options = {
//         weekday: "long",
//         day: "numeric",
//         month: "long"
//     };
    
//     var day=today.toLocaleDateString("en-US",options);

//     return day;
// }


// function getDay()
// {
//     var today= new Date();
//     var options = {
//         weekday: "long",
//     };
    
//     var day=today.toLocaleDateString("en-US",options);

//     return day;
// }





//Using Function expression way of declaring a function
exports.getDate=function () //module.exports.getDate=function () -->can also use this
{
    const today= new Date();
    const options = {
        weekday: "long",
        day: "numeric",
        month: "long"
    };
    
    var day=today.toLocaleDateString("en-US",options);

    return day;
}

exports.getDay=function()
{
    const today= new Date();
    const options = {
        weekday: "long",
    };
    
    var day=today.toLocaleDateString("en-US",options);

    return day;
}