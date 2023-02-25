/*
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código
*/

/*------------- Funções --------------*/ 
function Fibonacci(number){
    var x1 = 0;
    var x2 = 1;
    var sequence = 0;

    if(number == 0){
        return true;
    }
    if(number == 1){
        return true;
    }
    for(i = 0; i < number; i++){
        sequence = x1 + x2;
        x1 = x2;
        x2 = sequence;
        if(number == sequence){
            return true;
        }else if(sequence > number){
            return false;
        }
    }
}
/*---------------------------------------*/

var input = parseInt(prompt("Digite um número"));

if(Fibonacci(input)){
    alert("Esta na sequência!");
}else{
    alert("Não esta na sequência!");
}