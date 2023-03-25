let lengt = document.getElementById('length');
let gen = document.getElementById('gen');
let copyb = document.getElementById('copyb');
let password = document.getElementById('password');
gen.addEventListener('click',()=>{

  let charSet="0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let len=charSet.length;
  let pass='';
  for(let i=0;i<lengt.value;i++){
    let temp=Math.floor(Math.random()*len);
      pass+=charSet[temp];
    
  }

password.value = pass;

  
})
copyb.addEventListener('click', () => {
  password.select();
  document.execCommand('copy');
});
