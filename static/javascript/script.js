const inputText = document.getElementById('senha-gerada');
const copyButton = document.getElementById('copia-senha');

copyButton.addEventListener('click', execCopy);

function execCopy() {
    inputText.select();
    document.execCommand('copy');

    alert('Senha cópiada com sucesso!')
}