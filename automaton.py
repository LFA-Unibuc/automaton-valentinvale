class ValidationException(BaseException):
    pass


class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.states = []
        self.words = []
        self.transitions = []
        self.initial = []
        self.final = []
        self.dfaDict = {}
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """

        f = open(self.config_file)
        line = f.readline()
        while line.strip() != "Sigma :":
            if line.strip().split()[0] != "#":
                f.close()
                raise ValidationException
            line = f.readline()

        line = f.readline()
        while line.strip() != "End":
            if len(line.strip().split()) == 1:
                self.words.append(line.strip())
            else:
                f.close()
                raise ValidationException
            line = f.readline()

        line = f.readline()
        while line.strip() != "States :":
            if line.strip().split()[0] != "#":
                f.close()
                raise ValidationException
            line = f.readline()

        line = f.readline()
        nrS = 0
        nrF = 0

        while line.strip() != "End":
            if len(line.strip().split()) == 1:
                self.states.append(line.split(",")[0].strip())
            elif len(line.strip().split()) == 2:
                self.states.append(line.split(",")[0].strip())
                if line.strip().split(",")[1] == "F":
                    nrF = nrF + 1
                    self.final.append(line.strip().split(",")[0].replace(" ", ""))

                elif line.strip().split(",")[1] == "S":
                    nrS = nrS + 1
                    self.initial.append(line.strip().split(",")[0].replace(" ", ""))
                else:
                    f.close()
                    raise ValidationException
            elif len(line.strip().split()) == 3:
                self.states.append(line.split(",")[0].strip())
                if line.strip().split(",")[1] == "F" and line.strip().split(",")[2] == "S" or line.strip().split(",")[1] == "S" and line.strip().split(",")[2] == "F":
                    nrF = nrF + 1
                    nrS = nrS + 1
                    self.final.append(line.strip().split(",")[0].replace(" ", ""))
                    self.initial.append(line.strip().split(",")[0].replace(" ", ""))
                else:
                    f.close()
                    raise ValidationException
            else:
                f.close()
                raise ValidationException
            line = f.readline()

        if nrF == 0 or nrS == 0 or nrS > 1:
            raise ValidationException

        line = f.readline()
        while line.strip() != "Transitions :":
            if line.strip().split()[0] != "#":
                f.close()
                raise ValidationException
            line = f.readline()

        line = f.readline()
        while line.strip() != "End":
            if len(line.strip().split(",")) == 3:
                if line.split(",")[0].strip() not in self.states or line.split(",")[2].strip() not in self.states or line.split(",")[1].strip() not in self.words:
                    f.close()
                    raise ValidationException
            else:
                f.close()
                raise ValidationException
            self.transitions.append(line.strip())
            line = f.readline()

        f.close()

        d = {}

        for transition in self.transitions:
            state1, word, state2 = transition.split(",")
            state1 = state1.replace(" ", "")
            state2 = state2.replace(" ", "")
            word = word.replace(" ", "")

            if state1 not in d.keys():
                dt = {}
                if word not in dt.keys():
                    dt[word] = state2
                d[state1] = dt
            else:
                if word not in dt.keys():
                    d[state1][word] = state2

        self.dfaDict = d

        return True

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('input.txt')
    try:
        print(a.validate())
    except ValidationException:
        print("Validation Exception")
