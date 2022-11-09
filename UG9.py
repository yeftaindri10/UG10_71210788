class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority # 1 (tertinggi), 2, 3, 4, ...
        self._next = None

class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self._size
        
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty(): # kosong
            self._head = baru
            self._tail = baru
        else: # insert belakang
            self._tail._next = baru
            self._tail = baru
        self._size = self._size + 1

    def remove(self): # implementasi ini tidak return
        if self.is_empty() == False:
            if self._size == 1:
                bantu = self._head
                self._head = None
                self._tail = None
                del bantu
            else:
                # ambil prioritas pada head sebagai prioritas tertinggi yang diketahui
                min_priority = self._head._priority
                # cek dari head sampai tail, berapa prioritas tertinggi
                hapus = self._head
                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next
                # prioritas tertinggi sudah diketahui, letakkan hapus di node tersebut
                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next
                # cek yang akan dihapus itu head, tail, atau tengah?
                if hapus == self._head:
                    # hapus head
                    self._head = self._head._next
                    del hapus
                else:
                    # hapus tail atau tengah caranya sama saja
                    # letakkan bantu di posisi sebelum hapus
                    bantu = self._head
                    while bantu._next != hapus:
                        bantu = bantu._next
                    # hapus node
                    bantu._next = hapus._next
                    del hapus
                    # pastikan tail di posisi paling belakang
                    self._tail = self._head
                    while self._tail._next != None:
                        self._tail = self._tail._next
        self._size = self._size - 1
    
    def peek(self): # return dalam bentuk tuple (data, priority)
        if self.is_empty() == True:
            return None
        else:
            if self._size == 1:
                return tuple([self._head._data, self._head._priority])
            else:
                min_priority = self._head._priority
                bantu = self._head
                # cari nilai prioritas tertinggi
                while bantu != None:
                    if bantu._priority < min_priority:
                        min_priority = bantu._priority
                    bantu = bantu._next
                # nilai prioritas tertinggi sudah diketahui,
                # ambil nilai dan prioritas dari node tersebut
                bantu = self._head
                while bantu._priority != min_priority:
                    bantu = bantu._next
                return tuple([bantu._data, bantu._priority])
            
    def print_all(self):
        print("=== List UnSorted Queue ===")
        bantu = self._head
        while bantu != None:
            print(f"{bantu._priority} = {bantu._data}")
            bantu = bantu._next
        print() 
        # tuliskan kode Anda di sini
    
    def ubahBersama(self, prio, namaBaru):  # untuk mengubah data secara sekaligus
        bantu = self._head
        while bantu != None:
            if bantu._priority == prio:
                bantu._data = namaBaru
            bantu = bantu._next
        # tulis kode Anda di sini
    
    def removePrioSekaligus(self): # untuk menghapus data priority terkecil sekaligus
        bantu = self.peek()
        while bantu[1] == self.peek()[1]:
            self.remove()
        # tulis kode Anda di sini

    def fungsiTambahan(self): # Anda dapat membuat fungsi tambahan jika dibutuhkan    
        pass
        # tulis kode Anda di sini
        
myQueue = PriorityQueueUnsorted()
myQueue.add("Dedi",4)
myQueue.add("Sindu",2)
myQueue.add("Haniif",5)
myQueue.add("Farel",2)
myQueue.add("Beatrix",3)
myQueue.add("Shalom",3)
myQueue.add("Harris",2)
myQueue.print_all()

myQueue.ubahBersama(2,"Mahasiswa A")
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()