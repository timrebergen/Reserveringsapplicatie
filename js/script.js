function maak_afspraak() {
    let naam = document.getElementById('naam').value;
    let email = document.getElementById('email').value;
    let telefoonnummer = document.getElementById('telefoonnummer').value;
    let opmerkingen = document.getElementById('opmerkingen').value;
    let meeting_time = document.getElementById('meeting_time').value;
    let jsondata = { 'naam':naam, 'email':email, 'telefoonnummer':telefoonnummer, 'opmerkingen': opmerkingen, 'tijdstip': meeting_time};

    fetch('http://127.0.0.1:5000/afspraak', {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-type': 'application/json'},
        body: JSON.stringify(jsondata)
    }) .then((response) => {
        return response.json();
    }) .then((result) =>{
        alert(JSON.stringify(result));
    });
}
