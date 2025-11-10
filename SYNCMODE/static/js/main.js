async function carregarMusicas() {
    try {
        const resposta = await fetch("/scan");
        const musicas = await resposta.json();

        const lista = document.getElementById("lista-musicas");
        lista.innerHTML="";

        musicas.forEach(m => {
            const item = document.createElement("div");
            item.classList.add("musica-item");
           item.innerHTML = `
                <strong>${m.title}</strong><br>
                <span>${m.artist}</span>
                <small>BPM: ${m.bpm || '-'} | Key: ${m.key || '-'} | Duração: ${m.duration || '-'}s</small>`; 
            lista.appendChild(item);
        
        
        });

    

    } catch (erro) {
        console.error("erro ao carregar músicas:", erro);
    }
}

async function analisarFaixas(){
    const botao = document.getElementById("analisarBtn");
    botao.disabled = true;
    botao.innerText = "Analisando...";

    try {
        const resposta = await fetch("/scan");
        const musicas = await resposta.json();

        // lista específica do analisador (id alterado no HTML)
        const lista = document.getElementById("lista-analises");
        lista.innerHTML="";

        musicas.forEach(m => {
            const item = document.createElement("div");
            item.classList.add("musica-item");
            item.innerHTML = `
                <strong>${m.title}</strong><br>
                <span>${m.artist}</span><br>
                <small>BPM: ${m.bpm || '-'} | Key: ${m.key || '-'} | Duração: ${m.duration || '-'}s</small>`; 
                lista.appendChild(item);
        });
    }catch (erro) {
        console.error("Erro ao analisar faixas:", erro);
    }

    botao.disabled = false;
    botao.innerText = "Analisar Faixas";
}

/*item.innerHTML = `
        <strong>${m.title}</strong><br>
        <span>${m.artist}</span><br>
        <small>BPM: ${m.bpm || '-'} | Key: ${m.key || '-'} | Duração: ${m.duration || '-'}s</small>`;*/