def bayesSchritt(
        wurf: int,
        wahrscheinlichkeitenA: [float],
        wahrscheinlichkeitenB: [float],
        prior: (float, float)
    ) -> (float, float):
    '''
    Berechne die Wahrscheinlichkeit dafür, dass ein Wurf aus der Sequenz
    von Würfel A oder Würfel B kommt

    Args:
        wurf                  -- der aktuelle Wert des Würfels in der Sequenz
        wahrscheinlichkeitenA -- die Wahrscheinlichkeiten für die Seiten des Würfels A
        wahrscheinlichkeitenB -- die Wahrscheinlichkeiten für die Seiten des Würfels A
        prior                 -- die vorige Wahrscheinlichkeit für Würfel A und Würfel B
                                 als Tupel: (pA, pB)
    Returns:
        posterior             -- die Wahrscheinlichkeit für Würfel A und Würfel B
                                 als Tupel nach Beobachtung des aktuellen Wurfs: (pA, pB)
    '''
    # YOUR CODE HERE
    # Zahl 'wurf' wurde gewürfelt
    # P(A) und P(B) gesucht
    pMitA = wahrscheinlichkeitenA[wurf-1]
    pMitB = wahrscheinlichkeitenB[wurf-1]
    P_A = prior[0]
    P_B = prior[1]
    p_wurf = pMitA * P_A + pMitB * P_B

    result = ((pMitA * P_A)/p_wurf,(pMitB * P_B)/p_wurf)
    return result


    #P(A|B) = P(B|A)*P(A)/P(B)
    #P(A|B) die (bedingte) Wahrscheinlichkeit des Ereignisses  A unter der Bedingung, dass B eingetreten ist,
    #P(B∣A) die (bedingte) Wahrscheinlichkeit des Ereignisses B unter der Bedingung, dass A eingetreten ist,
    #P(A) die A-priori-Wahrscheinlichkeit des Ereignisses A und
    #P(B) die A-priori-Wahrscheinlichkeit des Ereignisses B.



#bayesSchritt(rd.randint(1,6),[1/6,1/6,1/6,1/6,1/6,1/6],[1/12,3/12,1/12,3/12,1/12,3/12],(0,0))
bayesSchritt(wurf = 1,
             wahrscheinlichkeitenA = [1/6,1/6,1/6,1/6,1/6,1/6],
             wahrscheinlichkeitenB = [1/12,3/12,1/12,3/12,1/12,3/12],
             prior = [0.5,0.5])
