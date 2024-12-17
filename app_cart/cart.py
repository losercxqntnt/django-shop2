from decimal import Decimal
from django.conf import settings
from app_store.models import SanPham


class GioHang:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        gio_hang = self.session.get(settings.CART_SESSION_ID)
        if not gio_hang:
            # save an empty cart in the session
            gio_hang = self.session[settings.CART_SESSION_ID] = {}
        self.gio_hang = gio_hang

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        danh_sach_san_pham_id = self.gio_hang.keys()
        # get the product objects and add them to the cart
        danh_sach_san_pham = SanPham.objects.filter(id__in=danh_sach_san_pham_id)

        gio_hang = self.gio_hang.copy()
        for san_pham in danh_sach_san_pham:
            gio_hang[str(san_pham.id)]['san_pham'] = san_pham

        for gh in gio_hang.values():
            gh['gia_ban'] = Decimal(gh['gia_ban'])
            gh['giam_gia'] = Decimal(gh['giam_gia'])
            gh['thanh_tien'] = gh['gia_ban'] * gh['so_luong'] * (1 - gh['giam_gia'])
            yield gh

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(gh['so_luong'] for gh in self.gio_hang.values())

    def them_vao_gio_hang(self, san_pham, so_luong=1):
        """
        Add a product to the cart or update its quantity.
        """
        san_pham_id = str(san_pham.id)
        if san_pham_id not in self.gio_hang:
            self.gio_hang[san_pham_id] = {'so_luong': so_luong, 'gia_ban': str(san_pham.gia_ban), 'giam_gia': '0'}
        else:
            self.gio_hang[san_pham_id]['so_luong'] += int(so_luong)
        self.luu_gio_hang()

    def luu_gio_hang(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def xoa_san_pham(self, san_pham):
        """
        Remove a product from the cart.
        """
        san_pham_id = str(san_pham.id)
        if san_pham_id in self.gio_hang:
            del self.gio_hang[san_pham_id]
            self.luu_gio_hang()

    def xoa_gio_hang(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.luu_gio_hang()

    def tong_tien_tam_tinh(self):
        return sum(Decimal(san_pham['gia_ban']) * san_pham['so_luong'] for san_pham in self.gio_hang.values())

    def tien_giam_gia(self):
        return sum(self.tong_tien_tam_tinh() * Decimal(san_pham['giam_gia']) for san_pham in self.gio_hang.values())

    def tong_tien_phai_tra(self):
        return self.tong_tien_tam_tinh() - self.tien_giam_gia()