# P107 — code sync from TRF (end-check code audit, 2 Nov): computed verdicts and exit codes in trf_checker/z3_check/
# crypto_envelope; docstring states a violation is a (record, constraint) pair; key-destruction comment and the crypto
# module's docstring and RESULT line say attested, not proven; demo_app requirements pinned. Blob-based, replays deterministically.
import subprocess
_b = lambda sha: subprocess.run(["git", "cat-file", "-p", sha], capture_output=True, text=True, check=True).stdout
LOST_OK = ["number 1.50", "number 42", "number 4.12"]
EDITS = [
 dict(id='P107-01', file='demo_app/trf_checker.py', old=_b("5710daf5829bdb05cd774f8f468fd584c325b1b4"), new=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), why="sync demo_app/trf_checker.py to TRF"),
 dict(id='P107-02', file='repro_package/trf_checker.py', old=_b("5710daf5829bdb05cd774f8f468fd584c325b1b4"), new=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), why="sync repro_package/trf_checker.py to TRF"),
 dict(id='P107-03', file='code_artefacts/trf_checker.py', old=_b("5710daf5829bdb05cd774f8f468fd584c325b1b4"), new=_b("d1a13aba57a223f149f34de63e413143eb93ba21"), why="sync code_artefacts/trf_checker.py to TRF"),
 dict(id='P107-04', file='demo_app/z3_check.py', old=_b("157e32ae52dfe6dfef20e0b72f8369cd0452425e"), new=_b("51bf3ced4517af5bd5f5c33495876484654243b4"), why="sync demo_app/z3_check.py to TRF"),
 dict(id='P107-05', file='repro_package/z3_check.py', old=_b("157e32ae52dfe6dfef20e0b72f8369cd0452425e"), new=_b("51bf3ced4517af5bd5f5c33495876484654243b4"), why="sync repro_package/z3_check.py to TRF"),
 dict(id='P107-06', file='code_artefacts/z3_check.py', old=_b("157e32ae52dfe6dfef20e0b72f8369cd0452425e"), new=_b("51bf3ced4517af5bd5f5c33495876484654243b4"), why="sync code_artefacts/z3_check.py to TRF"),
 dict(id='P107-07', file='demo_app/crypto_envelope.py', old=_b("53910abbec3540249e63fb9a839b695b8c22103d"), new=_b("80b0340159e36cb0cb2689535b955fec3bc3fc07"), why="sync demo_app/crypto_envelope.py to TRF"),
 dict(id='P107-08', file='repro_package/crypto_envelope.py', old=_b("53910abbec3540249e63fb9a839b695b8c22103d"), new=_b("80b0340159e36cb0cb2689535b955fec3bc3fc07"), why="sync repro_package/crypto_envelope.py to TRF"),
 dict(id='P107-09', file='code_artefacts/crypto_envelope.py', old=_b("53910abbec3540249e63fb9a839b695b8c22103d"), new=_b("80b0340159e36cb0cb2689535b955fec3bc3fc07"), why="sync code_artefacts/crypto_envelope.py to TRF"),
 dict(id='P107-10', file='repro_package/results/crypto_envelope_output.txt', old=_b("54aa05f2a10e1149a75b4107d4de065e68987f63"), new=_b("11ce9e03c7e43e47efde00271164843f2eb7a668"), why="sync repro_package/results/crypto_envelope_output.txt to TRF"),
 dict(id='P107-11', file='demo_app/requirements.txt', old=_b("52d470592b819e16577e05cfbae355fdfbbebeef"), new=_b("a3bc3d023d28546d559d21d219b4b32a232aa846"), why="sync demo_app/requirements.txt to TRF"),
]
