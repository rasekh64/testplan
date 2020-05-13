class Case:
    def __init__(self, reed, interval, y_n, z_n, alpha, beta, n_diameter, p_in):
        self.reed = reed
        self.interval = interval
        self.y_n = y_n
        self.z_n = z_n
        self.alpha = alpha
        self.beta = beta
        self.n_diameter = n_diameter
        self.p_in = p_in
        # self.speed = speed

    def reed_thickness(self):
        if self.reed == "Reed_1" or self.reed == "Reed_4" or self.reed == "Reed_8":
            reed_t = 0.2
            return reed_t
        elif self.reed == "Reed_2":
            reed_t = 0.28
            return reed_t
        else:
            reed_t = 0.4
            return reed_t
