import errno
import os

def full_read(fd, count):
    """
    Legge completamente 'count' byte da un file descriptor (fd).
    Gestisce eventuali interruzioni (EINTR) durante la lettura.

    Args:
        fd: File descriptor o socket da cui leggere.
        count: Numero massimo di byte da leggere.

    Returns:
        Un oggetto bytes con i dati letti.
    """
    nleft = count
    data = bytearray()

    while nleft > 0:
        try:
            chunk = os.read(fd, nleft)
            if not chunk:  # EOF
                break
            data.extend(chunk)
            nleft -= len(chunk)
        except OSError as e:
            if e.errno == errno.EINTR:
                continue
            else:
                raise

    return bytes(data)