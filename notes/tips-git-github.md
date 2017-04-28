## Dicas Git 

- cd : Entrar nas pastas.
- ls : Verificar o que tem nas pastas.

- git init: iniciar git
- git clone /caminho/para/o/repositório : Clonar repositório remoto pro local.
- touch “nome do arquivo que deseja criar”: Criar um novo arquivo.
- git add <arquivos...>: Este comando adiciona o(s) arquivo(s) em um lugar que chamamos de INDEX, que funciona como uma área do git no qual os arquivos possam ser enviados ao Github. É importante saber que ADD não está adicionando um arquivo novo ao repositório, mas sim dizendo que o arquivo (sendo novo ou não) está sendo preparado para entrar na próxima revisão do repositório. Se usar git add * (significa add tudo).
- git commit -m "comentário qualquer": Este comando realiza o que chamamos de “commit”, que significa pegar todos os arquivos que estão naquele lugar INDEX que o comando add adicionou e criar uma revisão com um número e um comentário, que será vista por todos
- git push (empurrar): É usado para publicar todos os seus commits para o github. Neste momento, será pedido a sua senha.
- git pull (puxar): para atualizar seu repositório local com a mais nova versão.
- git status : Exibe o status do seu repositório atual.



Fontes:

http://rogerdudler.github.io/git-guide/index.pt_BR.html <br/>
https://tableless.com.br/tudo-que-voce-queria-saber-sobre-git-e-github-mas-tinha-vergonha-de-perguntar/


-------------------------------------------------------------------------------
# [Curso Git e Github](https://willianjusten.com.br/cursos/)

Curso do Willian Justen, oferecido gratuitamente.

### Configurando o git

- Configurar o usename: git config --global user.name “Nome do usuário” <br/>
- Configurar o email: git config --global user.email “email do usuário” <br/>
- Configurar editor principal git: git config --global core.editor sub  //sub significa sublime, senão for definido, por padrão é vim <br/>


Para saber as informações que você colocou nas configurações:

- git config user.name  (mostra username cadastrado) <br/>
- git config user.email (mostra e-mail cadastrado) <br/>
- git config --list (mostra tudo) <br/>

### Iniciando um repositório

- mkdir nomedapasta (criar pasta)
- cd nomedapasta (entra na pasta)
- git init (iniciar repositório)
- ls -la (mostra literalmente tudo, permissão, etc)
- ls (mostra pastas, arquivos)
- cd .. (volta um diretório)


### O ciclo de vida dos status de seus arquivos

- git status (reportar como está o repositório no momento)
- git add nomedoarquivo
- git commit -m “comentário”

**Boa prática colocar nos comentários o que você realmente fez**

### Visualizando logs

- git log (mostra os logs)
- git log --decorate (mostra outras informações)
- git log --author= “nome do autor” (mostra informações e alterações do autor)
- git shortlog (quais foram os autores, quais commits foram feitos)
- git shortlog -sn (mostrar só a quantidade de commit e nome)
- git log --graph (forma gráfica com seus branches e suas versões)
- git show (adicionar o número da hash(código do commit), pra ver o que foi feito)

### Visualizando o diff

Alterei um arquivo e após usei o diff <br/>
- git diff (mostra as alterações, antes de commitar)
- git diff --name-only (aparece só os nomes dos arquivos)
- git commit -am “comentário” (coomitar todos os arquivos modificados, a = all, m = message)

### Desfazendo coisas

- git checkout (retorna arquivo antes da edição)
- git reset HEAD nome do arquivo  //(remover da fila do staged)
- git reset --soft --mixed --hard numero da hash
	exemplo: git reset –soft b4f3rtertgd5453(hash) <br/>
	soft = matar commit, o arquivo continuar no staged <br/>
	mixed = matar commit, voltar os arquivos pra antes do staged, pro modified <br/>
	hard = ignorar existência commit e tudo que foi feito <br/>
	hash = um código alfanumérico que atribuído para cada commit <br/>

### Branch

- git checkout -b nome do branch
- git checkout nome do branch (pra entrar no branch)
- git branch -D testing (deletar branch)
- git branch (mostrar os branches)

Para unir branches, se usa merge ou rebase <br/>
Para entender melhor: [Merge e Rebase diferenças](http://www.arruda.blog.br/programacao/dicas-de-git-rebase-vs-merge/) <br/>

### Stash

- git stash (guardar modificações que não foram comitadas em um arquivo e que você possa chamar quando for necessário)
- git stash apply (vai aplicar as modificações)
- git stash list (lista de todos os stashs que estou fazendo)
- git stash clear (limpar todos stash)


### Alias
É um atalho dos comandos, pra facilitar o dia a dia <br/>

- git config --global alias.s coloqueocomando  
	exemplo: git status , você pode criar atalho como git config --global alias.s , o s corresponde ao status.


### Tag

- git tag -a 1.0.0 -m “comentário” (adicionar uma tag)
- git push origin master –tags (subir tags para servidor remoto)


### Revert

- git revert “hash do commit” (reverte o commit, apaga a alteração, mas não some com o commit)


### Apagando tags e branches remotos

- git tag -d nomedatag (apaga a tag)
- git push origin : nomedatag (apagar remotamente)
- git push origin : nomedabranch (apaga branch remotamente)
