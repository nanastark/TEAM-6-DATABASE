CREATE DATABASE perpusnas;

USE perpusnas;

CREATE TABLE perpustakaannasional(
nama_buku varchar(100),
penulis_buku varchar(100),
nomor_isbn varchar(100),
tahun_penelitian varchar(100)
);

CREATE TABLE penilaian(
judul_buku varchar(100),
penulis_buku varchar(50),
penilaian varchar(100)
);

select * from perpustakaan nasional;
select * from penilaian;