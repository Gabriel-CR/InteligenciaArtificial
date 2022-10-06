import java.util.HashMap;
import java.util.Map;

public class Data {
    private Map<Estado, Estado[]> listaAdjacencias = new HashMap<Estado, Estado[]>();

    private Estado[] estados = new Estado[] {
        new Estado("Oradea"),           // 0
        new Estado("Zerind"),           // 1
        new Estado("Arad"),             // 2
        new Estado("Sibiu"),            // 3
        new Estado("Timisoara"),        // 4
        new Estado("Lugoj"),            // 5
        new Estado("Mehadia"),          // 6
        new Estado("Drobeta"),          // 7
        new Estado("Fagaras"),          // 8
        new Estado("Rimmieu Vilcea"),   // 9 
        new Estado("Craiova"),          // 10
        new Estado("Pitesti"),          // 11
        new Estado("Giurgi"),           // 12
        new Estado("Bucharest"),        // 13
        new Estado("Urziceni"),         // 14
        new Estado("Hirsova"),          // 15
        new Estado("Eforie"),           // 16
        new Estado("Vaslui"),           // 17
        new Estado("Iasi"),             // 18
        new Estado("Neamt")             // 19
    };

    public Data(){
        listaAdjacencias.put(estados[0], new Estado[] {    // Oradea
            new Estado(estados[2].getNome()),
            new Estado(estados[3].getNome())
        });
    
        listaAdjacencias.put(estados[1], new Estado[] {    // Zerind
            new Estado(estados[0].getNome()),
            new Estado(estados[2].getNome())
        });
    
        listaAdjacencias.put(estados[2], new Estado[] {    // Arad
            new Estado(estados[1].getNome()),
            new Estado(estados[3].getNome()),
            new Estado(estados[4].getNome())
        });
    
        listaAdjacencias.put(estados[3], new Estado[] {    // Sibiu
            new Estado(estados[0].getNome()),
            new Estado(estados[2].getNome()),
            new Estado(estados[8].getNome()),
            new Estado(estados[9].getNome())
        });
    
        listaAdjacencias.put(estados[4], new Estado[] {    // Timisoara
            new Estado(estados[2].getNome()),
            new Estado(estados[5].getNome())
        });
    
        listaAdjacencias.put(estados[5], new Estado[] {    // Lugoj
            new Estado(estados[4].getNome()),
            new Estado(estados[6].getNome())
        });
    
        listaAdjacencias.put(estados[6], new Estado[] {    // Mehadia
            new Estado(estados[5].getNome()),
            new Estado(estados[7].getNome())
        });
    
        listaAdjacencias.put(estados[7], new Estado[] {    // Drobeta
            new Estado(estados[6].getNome()),
            new Estado(estados[10].getNome())
        });
    
        listaAdjacencias.put(estados[8], new Estado[] {    // Fagaras
            new Estado(estados[3].getNome()),
            new Estado(estados[13].getNome())
        });
    
        listaAdjacencias.put(estados[9], new Estado[] {    // Rimmieu Vilcea
            new Estado(estados[3].getNome()),
            new Estado(estados[11].getNome()),
            new Estado(estados[10].getNome())
        });
    
        listaAdjacencias.put(estados[10], new Estado[] {   // Craiova
            new Estado(estados[7].getNome()),
            new Estado(estados[9].getNome()),
            new Estado(estados[11].getNome())
        });
    
        listaAdjacencias.put(estados[11], new Estado[] {   // Pitesti
            new Estado(estados[9].getNome()),
            new Estado(estados[10].getNome()),
            new Estado(estados[13].getNome())
        });
    
        listaAdjacencias.put(estados[12], new Estado[] {   // Giurgi
            new Estado(estados[13].getNome())
        });
    
        listaAdjacencias.put(estados[13], new Estado[] {   // Bucharest
            new Estado(estados[8].getNome()),
            new Estado(estados[11].getNome()),
            new Estado(estados[12].getNome()),
            new Estado(estados[14].getNome())
        });
    
        listaAdjacencias.put(estados[14], new Estado[] {   // Urziceni
            new Estado(estados[13].getNome()),
            new Estado(estados[15].getNome()),
            new Estado(estados[17].getNome())
        });
    
        listaAdjacencias.put(estados[15], new Estado[] {   // Hirsova
            new Estado(estados[14].getNome()),
            new Estado(estados[16].getNome())
        });
    
        listaAdjacencias.put(estados[16], new Estado[] {   // Eforie
            new Estado(estados[15].getNome())
        });
    
        listaAdjacencias.put(estados[17], new Estado[] {   // Vaslui
            new Estado(estados[14].getNome()),
            new Estado(estados[18].getNome())
        });
    
        listaAdjacencias.put(estados[18], new Estado[] {   // Iasi
            new Estado(estados[17].getNome()),
            new Estado(estados[19].getNome())
        });
    
        listaAdjacencias.put(estados[19], new Estado[] {   // Neamt
            new Estado(estados[18].getNome())
        });
    }

    public Map<Estado, Estado[]> getListaAdjacencias() {
        return listaAdjacencias;
    }

    public Estado[] getEstados() {
        return estados;
    }
}
