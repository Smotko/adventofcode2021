from rich.progress import track
import math
import statistics
import heapq
from dataclasses import dataclass
from collections import Counter, defaultdict

from utils import get_input, submit, console
from itertools import pairwise, product
import binascii


inp = get_input(15, no_split=True)
inp = """0052E4A00905271049796FB8872A0D25B9FB746893847236200B4F0BCE5194401C9B9E3F9C63992C8931A65A1CCC0D222100511A00BCBA647D98BE29A397005E55064A9DFEEC86600BD002AF2343A91A1CCE773C26600D126B69D15A6793BFCE2775D9E4A9002AB86339B5F9AB411A15CCAF10055B3EFFC00BCCE730112FA6620076268CE5CDA1FCEB69005A3800D24F4DB66E53F074F811802729733E0040E5C5E5C5C8015F9613937B83F23B278724068018014A00588014005519801EC04B220116CC0402000EAEC03519801A402B30801A802138801400170A0046A800C10001AB37FD8EB805D1C266963E95A4D1A5FF9719FEF7FDB4FB2DB29008CD2BAFA3D005CD31EB4EF2EBE4F4235DF78C66009E80293AE9310D3FCBFBCA440144580273BAEE17E55B66508803C2E0087E630F72BCD5E71B32CCFBBE2800017A2C2803D272BCBCD12BD599BC874B939004B5400964AE84A6C1E7538004CD300623AC6C882600E4328F710CC01C82D1B228980292ECD600B48E0526E506F700760CCC468012E68402324F9668028200C41E8A30E00010D8B11E62F98029801AB88039116344340004323EC48873233E72A36402504CB75006EA00084C7B895198001098D91AE2190065933AA6EB41AD0042626A93135681A400804CB54C0318032200E47B8F71C0001098810D61D8002111B228468000E5269324AD1ECF7C519B86309F35A46200A1660A280150968A4CB45365A03F3DDBAE980233407E00A80021719A1B4181006E1547D87C6008E0043337EC434C32BDE487A4AE08800D34BC3DEA974F35C20100BE723F1197F59E662FDB45824AA1D2DDCDFA2D29EBB69005072E5F2EDF3C0B244F30E0600AE00203229D229B342CC007EC95F5D6E200202615D000FB92CE7A7A402354EE0DAC0141007E20C5E87A200F4318EB0C"""
# inp = """CE00C43D881120"""


class Parser:
    def __init__(self, binary):
        self.binary = binary
        self.position = 0
        self.versions = []
        self.result = int(self.parse())

    def read_next(self, num, debug=False):
        if debug:
            console.log(self.binary)
            console.log(" " * self.position + "^" * num)
        r = self.binary[self.position : self.position + num]
        self.position += num

        return r

    def read_next_int(self, num, debug=False):
        return int(self.read_next(num, debug), 2)

    def parse(self):
        version = int(self.read_next(3, debug=False), 2)
        self.versions.append(version)
        p_id = int(self.read_next(3), 2)

        if p_id == 4:
            parsed_number = ""
            while True:
                num = self.read_next(5)
                parsed_number += num[1:]
                if num[0] == "0":
                    break
            return int(parsed_number, 2)

        else:
            length_type_id = self.read_next(1)
            vals = []
            if length_type_id == "0":
                actual_length = int(self.read_next(15, debug=False), 2)
                terminate_at = self.position + actual_length
                while self.position != terminate_at:
                    vals.append(self.parse())
            else:
                num_subpackets = self.read_next_int(11)
                for _ in range(num_subpackets):
                    vals.append(self.parse())
            match p_id:
                case 0:
                    return sum(vals)
                case 1:
                    return math.prod(vals)
                case 2:
                    return min(vals)
                case 3:
                    return max(vals)
                case 5:
                    return vals[0] > vals[1]
                case 6:
                    return vals[0] < vals[1]
                case 7:
                    return vals[0] == vals[1]

p = Parser(bin(int("f" + inp, 16)).replace("0b1111", ""))
console.log(sum(p.versions), p.result)
