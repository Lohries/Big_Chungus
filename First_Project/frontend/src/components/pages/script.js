async function readRoot() {
    const response = await fetch ('http://localhost:8000/');
    const data = await response.json();
    console.log(data);
}

async function storeImage() {
    const response = await fetch ('http://localhost:8000/store/');
    const data = await response.json();
    console.log(data);

}
async function analyzePerson() {
    const response = await fetch ('http://localhost:8000/analyze/');
    const data = await response.json();
    console.log(data);

}

async function verifyPerson()  {
    const response = await fetch ('http://localhost:8000/verify/');
    const data = await response.json();
    console.log(data); 


}
