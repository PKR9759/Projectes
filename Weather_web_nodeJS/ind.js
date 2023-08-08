const http= require('http');
const fs= require('fs');
const requests= require('requests');

const home=fs.readFileSync("index.html",'utf-8');

const replVal=(tmp,real)=>{//Here we used tmpr variable to store resultant dtaa after replacement becuse replace not change original data but return it
    let tempr=tmp.replace("[%temp%]",(real.main.temp-273.15).toFixed(2));// tmp is our html file and real is our api data
     tempr=tempr.replace("[%city%]",real.name);
     tempr=tempr.replace("[%country%]",real.sys.country);
     return tempr;
}
const server=http.createServer((req, res) => {

    if(req.url=="/"){
        requests("https://api.openweathermap.org/data/2.5/weather?q=Nadiad&appid=bd1b1dea813f59ea88547a79ed2304e1",)
        .on("data", (data) =>{ 
            const objd=JSON.parse(data);
            let arr=[objd]
            // console.log(arr);

            const realTimeData=arr.map(val=> replVal(home, val)).join("");
            res.write(realTimeData);
        }) 
        .on("end", (err) =>{
            if(err) return console.log("Connection closed due to erorrs",err);
            // console.log('end');
            res.end();
        });   
    } 
});
server.listen(8000,"127.0.0.1");




