function search(){
    let searchTerm = document.getElementById('searchField').value.toLowerCase();
    let allNotes = document.getElementsByClassName("note");
    for(let i = 0; i < allNotes.length; i++){
        let textMatch = (allNotes[i].children[0].innerText.toLowerCase().indexOf(searchTerm) >= 0) || (allNotes[i].children[1].innerText.toLowerCase().indexOf(searchTerm) >= 0) 
        if(textMatch){ allNotes[i].style.display = "block"; }
        else{ allNotes[i].style.display = "none"; }
    }
}