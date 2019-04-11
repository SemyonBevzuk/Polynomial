class Polynomial:
    #def get_coefficients(self):
    #    return self.__coefficients
    #__coefficients = [0]

    def degree(self):
        return len(self.__coefficients) - 1

    def __init__(self, *args):
        if not args:
            self.__coefficients = [0]
        elif isinstance(args[0], (tuple, list, Polynomial)):
            if isinstance(args[0], Polynomial):
                self.__coefficients = [a for a in args[0].coeffs]
            elif args[0] or len(args[0]) != 0:
                if self.__is_list_correct(list(args[0])):
                    self.__coefficients = self.__remove_zeros_list(list(args[0]))
                else:
                    raise ValueError('Invalid argument in init. The list/tuple must store int.')
            else:
                self.__coefficients = [0]
        else:
            raise TypeError('Invalid argument in init. Need nothing, Polynomial, list or tuple.')

    def __is_list_correct(self, coefficients):
        result = True
        for a in coefficients:
            if not isinstance(a, int):
                result = False
                break
        return result

    def __remove_zeros_list(self, coefficients):
        short_coefficients = []
        flag_no_first_nonzero = True
        for a in coefficients:
            if a == 0 and flag_no_first_nonzero:
                continue
            else:
                flag_no_first_nonzero = False
                short_coefficients.append(a)
        if flag_no_first_nonzero:
            short_coefficients.append(0)
        return short_coefficients

    def __remove_zeros_polynomial(self):
        self.__coefficients = self.__remove_zeros_list(self.__coefficients)

    def __str__(self):
        string = ''
        i = 0
        current_degree = self.degree()
        if current_degree == 0:
            #if self.__coefficients[i] != 0:
            if self.__coefficients[i] < 0:
                string += '- '
            string += str(abs(self.__coefficients[i]))
        else:
            if self.__coefficients[i] < 0:
                string += '- '
            if abs(self.__coefficients[i]) != 1:
                string += str(abs(self.__coefficients[i]))
            if current_degree != 0:
                if current_degree != 1:
                    string += 'x^' + str(current_degree)
                else:
                    string += 'x'
            current_degree -= 1
            i += 1
            while current_degree >= 0:
                if self.__coefficients[i] != 0:
                    if self.__coefficients[i] < 0:
                        string += ' - '
                    else:
                        string += ' + '
                    if abs(self.__coefficients[i]) != 1 or current_degree == 0:
                        string += str(abs(self.__coefficients[i]))
                    if current_degree != 0:
                        if current_degree != 1:
                            string += 'x^' + str(current_degree)
                        else:
                            string += 'x'
                current_degree -= 1
                i += 1
        return string

    def __repr__(self):
        return 'Polynomial({})'.format(str(self.__coefficients))

    def __call__(self, x):
        if isinstance(x, (int, float)):
            res = 0
            for i, a in enumerate(self.coeffs):
                res += a * x ** (self.degree() - i)
            return res
        else:
            raise TypeError('Invalid argument in call. Need int or float.')

    def __iter__(self):
        for a in self.__coefficients:
            yield a

    def __getitem__(self, degree):
        if isinstance(degree, int):
            if degree >= 0:
                index = self.degree() - degree
                if index >= 0:
                    return self.__coefficients[index]
                else:
                    return 0
            else:
                raise ValueError('Invalid argument in getitem. Need int >= 0.')
        else:
            raise TypeError('Invalid argument in getitem. Need int >= 0.')

    def __setitem__(self, degree, value):
        if isinstance(degree, int) and isinstance(value, int):
            if degree >= 0:
                if degree <= self.degree():
                    index = self.degree() - degree
                    del self.__coefficients[index]
                    self.__coefficients.insert(index, value)
                else:
                    differences = degree - self.degree() - 1
                    zeros = [0]*differences
                    self.__coefficients = zeros + self.__coefficients
                    self.__coefficients.insert(0, value)
                self.__remove_zeros_polynomial()
            else:
                raise ValueError('Invalid argument in setitem. For degree need: int >= 0.')
        else:
            raise TypeError('Invalid argument in setitem. For degree need: int >= 0. For value need: int.')

    def __getattr__(self, arg):
        if arg == 'coeffs':
            return self.__coefficients
        else:
            raise AttributeError('Invalid attribute in getattr. Use <Polynomial_name>.coeffs.')

    def __setattr__(self, arg, list_coeffs):
        if arg == 'coeffs' or arg == '_Polynomial__coefficients':
            if isinstance(list_coeffs, (list, tuple)):
                if self.__is_list_correct(list(list_coeffs)):
                    self.__dict__[arg] = list_coeffs
                else:
                    raise ValueError('Invalid argument in setattr. The list/tuple must store int.')
            else:
                raise TypeError('Invalid argument in setattr. Use list or tuple.')
        else:
            raise AttributeError('Invalid attribute in setattr. Use <Polynomial_name>.coeffs.')

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            raise TypeError('Invalid argument in ==. Need Polynomial.')

    def __ne__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs != other.coeffs
        else:
            raise TypeError('Invalid argument in !=. Need Polynomial.')

    def __neg__(self):
        return Polynomial([-a for a in self.coeffs])

    def __pos__(self):
        return self

    @staticmethod
    def zip_two_polynomial(poly1, poly2):
        longest_polynomial = ''
        max_len = 0
        min_len = 0
        if len(poly1.coeffs) >= len(poly2.coeffs):
            max_len = len(poly1.coeffs)
            min_len = len(poly2.coeffs)
            longest_polynomial = '1'
        else:
            max_len = len(poly2.coeffs)
            min_len = len(poly1.coeffs)
            longest_polynomial = '2'
        differences = max_len - min_len

        j = min_len - 1
        for i in range(max_len-1, -1, -1):
            if i >= differences and longest_polynomial == '1' and max_len != min_len:
                yield (poly1[i], 0)
            elif i >= differences and longest_polynomial == '2' and max_len != min_len:
                yield (poly2[i], 0)
            elif longest_polynomial == '1':
                yield (poly1[i], poly2[j])
                j -= 1
            else:
                yield (poly2[i], poly1[j])
                j -= 1

    def __add__(self, other):
        if isinstance(other, Polynomial):
            res = [a + b for a, b in Polynomial.zip_two_polynomial(self, other)]
            return Polynomial(res)
        elif isinstance(other, int):
            res = self.coeffs
            res[self.degree()] += other
            return Polynomial(res)
        else:
            raise TypeError('Invalid argument in add. Need Polynomial or int.')

    def __radd__(self, other):
        if isinstance(other, int):
            res = self.coeffs
            res[self.degree()] += other
            return Polynomial(res)
        else:
            raise TypeError('Invalid argument in radd. Need int.')

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            res = [a - b for a, b in Polynomial.zip_two_polynomial(self, other)]
            return Polynomial(res)
        elif isinstance(other, int):
            res = self.coeffs
            res[self.degree()] -= other
            return Polynomial(res)
        else:
            raise TypeError('Invalid argument in sub. Need Polynomial or int.')

    def __rsub__(self, other):
        if isinstance(other, int):
            return -self + other
        else:
            raise TypeError('Invalid argument in rsub. Need int.')

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            res_degree = self.degree() + other.degree()
            res = [0] * (res_degree + 1)
            for index_a, a in enumerate(self.coeffs):
                for index_b, b in enumerate(other.coeffs):
                    degree_a = self.degree() - index_a
                    degree_b = other.degree() - index_b
                    index_res = res_degree - (degree_a + degree_b)
                    res[index_res] = res[index_res] + a * b
            return Polynomial(res)
        elif isinstance(other, int):
            res = [other * a for a in self.coeffs]
            return Polynomial(res)
        else:
            raise TypeError('Invalid argument in mul. Need Polynomial or int.')

    def __rmul__(self, other):
        if isinstance(other, int):
            res = [other * a for a in self.coeffs]
            return Polynomial(res)
        else:
            raise TypeError('Invalid argument in rmul. Need Polynomial or int.')
