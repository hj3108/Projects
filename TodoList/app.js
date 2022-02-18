const express= require("express");
const bodyParser= require("body-parser");
const date=require(__dirname+"/date.js");

const app= express();

// if we apply const to apply arrays we can push any item in array but cannot completely reassign
// it with something.
const items = ["Buy Food" , "Cook Food", "Eat Food"];
const workItems= [];

app.set('view engine','ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/",function(req,res){

    const day=date.getDate();

    res.render('list', {listTitle: day, newListItems: items}); //here it doesn't have value to be added to newListItem
    // that's why our app crashes
 
});

// When we press the submit button our form is going to make a post request
// to the home route("/") and it's going to post the value of  text input
// which has a name of "newItem". When that request gets received it gets called inside
// app.post() section and we tap into that post request and we search for the value named 
// "newItem".

app.post("/",function(req,res)
{
    const item=req.body.newItem;
    // console.log(req.body);

    if(req.body.list==="Work")
    {
        if(item.length>0)
        {
            workItems.push(item);
        }
        res.redirect("/work");
    }
    else
    {
        if(item.length>0)
        {
            items.push(item);
        }
        res.redirect("/"); //what it does is when the post request is triggered in the home route
        // will save the value of newItem inside that text box to a variable called item and
        // it will redirect to the home route which then moves us to "app.get()" and will trigger it and will
        // res.render() the list template passing both the values
    }
    
        
    // console.log(item);
    // res.render('list', {newListItem: item}); //instead of this as we have rendered this value above

   
});

app.get("/work",function(req,res)
{
    res.render('list', {listTitle: "Work List", newListItems: workItems})
});

// app.post("/work",function(req,res)
// {
//     var item=req.body.newItem;
//     if(item.length>0)
//     {
//         workItems.push(item);
//     }
//     res.redirect("/work");
// });

app.get("/about",function(req,res)
{
    res.render("about");
});



app.listen(process.env.PORT || 3000,function(){
    console.log("Server is running on port 3000.");
});

