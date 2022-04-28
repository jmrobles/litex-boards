#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2022 JM Robles <roblesjm@gmail.com>
# Copyright (c) 2020 David Corrigan <davidcorrigan714@gmail.com>
# Copyright (c) 2020 Alan Green <avg@google.com>
# Copyright (c) 2020 David Shah <dave@ds0.me>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform
from litex.build.lattice.programmer import LatticeProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Appendix A. Figure A.6 EVDK and HiMax Cameras (clocks)
    ("clk27", 0, Pins("R11"), IOStandard("LVCMOS18H")),
    ("clk24", 0, Pins("N14"), IOStandard("LVCMOS18")),

    # 8. Input switches and pushbuttons
    ("user_dip_btn", 0, Pins("R5"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 1, Pins("T4"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 2, Pins("R7"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 3, Pins("T8"), IOStandard("LVCMOS18")),
    ("user_btn", 0, Pins("K2"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("L1"), IOStandard("LVCMOS33")),
    ("gsrn", 0, Pins("L2"), IOStandard("LVCMOS33")),
    ("program", 0, Pins("D13"), IOStandard("LVCMOS33")),
    ("cam_reset", 0, Pins("N15"), IOStandard("LVCMOS18H"), Misc("PULLMODE=UP")),  # SW1

    # 7. LEDs
    ("user_led", 0, Pins("H1"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("J1"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("H5"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("H6"), IOStandard("LVCMOS33")),
    ("user_led_rgb", 0, Pins("J7 J6 J2"), IOStandard("LVCMOS33")),
    ("user_led_rgb", 1, Pins("J3 J4 J5"), IOStandard("LVCMOS33")),

    # HyperRAM
    ("hyperram", 0,
        Subsignal("dq", Pins("U5 U6 T6 N6 P6 U7 U8 T7"), IOStandard("LVCMOS18H")),
        Subsignal("rwds", Pins("U4"), IOStandard("LVCMOS18H")),
        Subsignal("cs_n", Pins("N5"), IOStandard("LVCMOS18H")),
        Subsignal("rst_n", Pins("P5"), IOStandard("LVCMOS18H")),
        Subsignal("clk", Pins("R4"), IOStandard("LVDS")),
        # Subsignal("clk_n", Pins("P4"), IOStandard("LVDS")),
        Misc("SLEWRATE=FAST")

    ),
    ("hyperram", 1,
        Subsignal("dq", Pins("P8 N8 U9 U10 T10 R10 P9 N9"), IOStandard("LVCMOS18H")),
        Subsignal("rwds", Pins("N7"), IOStandard("LVCMOS18H")),
        Subsignal("cs_n", Pins("T9"), IOStandard("LVCMOS18H")),
        Subsignal("rst_n", Pins("P7"), IOStandard("LVCMOS18H")),
        Subsignal("clk", Pins("T11"), IOStandard("LVDS")),
        # Subsignal("clk_n", Pins("U11"), IOStandard("LVDS")),
        Misc("SLEWRATE=FAST")

    ),
    # SPI Flash
    ("spiflash", 0,
        Subsignal("cs_n", Pins("C14")),
        Subsignal("clk", Pins("D16")),
        Subsignal("mosi", Pins("C13")),
        Subsignal("miso", Pins("C16")),
        Subsignal("wp", Pins("C17")),
        Subsignal("hold", Pins("B16")),
        IOStandard("LVCMOS33")
    ),
    ("spiflash4x", 0,
        Subsignal("cs_n", Pins("C14")),
        Subsignal("clk", Pins("D16")),
        Subsignal("dq", Pins("C13 C16 C17 B16")),
        IOStandard("LVCMOS33")
    ),
    # Microphones
    # TODO
    # Camera I2C bus
    ("i2c", 0,
        Subsignal("scl", Pins("R15")),
        Subsignal("sda", Pins("U15")),
        IOStandard("LVCMOS18H")

    ),
    # Camera HiRes
    ("camera_mclk", 0, Pins("M14"), IOStandard("LVCMOS18H")),
    ("camera", 0,
        Subsignal("clkp", Pins("D1")),
        Subsignal("clkn", Pins("E2")),
        Subsignal("dp", Pins("E1 C1 F1 B1")),
        Subsignal("dn", Pins("F2 D2 G2 C2")),
    ),
    ("cam_ctrl",
        Subsignal("cam_reset", Pins("N15")),
        Subsignal("cam_frame_sync", Pins("P15")),
        IOStandard("LVCMOS18")
    ),
    # Serial port
    ("serial", 0,
        Subsignal("rx", Pins("B17"), IOStandard("LVCMOS33")),
        Subsignal("tx", Pins("A16"), IOStandard("LVCMOS33")),
    ),
    # Camera LoRes
    # TODO
    
    # CYUSB3014
    # TODO
]


# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    # MIPI DPHY
    ("MIPI_DPHY", {
        "DPHY1_CKP": "A4",
        "DPĤY1_DP1": "A5",
        "DPHY1_CKN": "B4",
        "DPHY1_DN1": "B5",
        "DPHY1_DP0": "A3",
        "DPHY1_DP2": "A2",
        "DPHY1_DN0": "B3",
        "DPHY1_DN2": "B2",
        "I2C_DPHY1_SCL": "T17",
        "DPHY1_DP3": "A6",
        "I2C_DPHY1_SDA": "T16",
        "DPHY1_DN3": "B6"
    }),
    # PMOD signal number:
    #          1   2  3  4  7  8  9   10
    ("PMOD0", "D7 D6 E7 E6 D4 D5 E5 E4"),
    ("PMOD1", "F7 F6 H3 H4 G7 G6 H7 H8"),
    ("PMOD2", "L13 L12 L11 L10 K11 K10 K17 K16"),
    ("PMOD3", "J17 J16 J15 J14 J13 J12 J11 J10"),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name   = "clk27"
    default_clk_period = 1e9/27e6

    def __init__(self, device="LIFCL", toolchain="radiant", **kwargs):
        assert device in ["LIFCL"]
        LatticePlatform.__init__(self, device + "-40-8MG289C", _io, _connectors, toolchain=toolchain, **kwargs)

    def create_programmer(self, mode = "direct"):
        assert mode in ["direct","flash"]

        xcf_template_direct = """<?xml version='1.0' encoding='utf-8' ?>
<!DOCTYPE       ispXCF  SYSTEM  "IspXCF.dtd" >
<ispXCF version="R1.2.0">
    <Comment></Comment>
    <Chain>
        <Comm>JTAG</Comm>
        <Device>
            <SelectedProg value="TRUE"/>
            <Pos>1</Pos>
            <Vendor>Lattice</Vendor>
            <Family>LIFCL</Family>
            <Name>LIFCL-40</Name>
            <IDCode>0x010f1043</IDCode>
            <Package>All</Package>
            <PON>LIFCL-40</PON>
            <Bypass>
                <InstrLen>8</InstrLen>
                <InstrVal>11111111</InstrVal>
                <BScanLen>1</BScanLen>
                <BScanVal>0</BScanVal>
            </Bypass>
            <File>{bitstream_file}</File>
            <JedecChecksum>N/A</JedecChecksum>
            <MemoryType>Static Random Access Memory (SRAM)</MemoryType>
            <Operation>Fast Configuration</Operation>
            <Option>
                <SVFVendor>JTAG STANDARD</SVFVendor>
                <IOState>HighZ</IOState>
                <PreloadLength>362</PreloadLength>
                <IOVectorData>0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF</IOVectorData>
                <Usercode>0x00000000</Usercode>
                <AccessMode>Direct Programming</AccessMode>
            </Option>
        </Device>
    </Chain>
    <ProjectOptions>
        <Program>SEQUENTIAL</Program>
        <Process>ENTIRED CHAIN</Process>
        <OperationOverride>No Override</OperationOverride>
        <StartTAP>TLR</StartTAP>
        <EndTAP>TLR</EndTAP>
        <VerifyUsercode value="FALSE"/>
        <TCKDelay>3</TCKDelay>
    </ProjectOptions>
    <CableOptions>
        <CableName>USB2</CableName>
        <PortAdd>FTUSB-0</PortAdd>
    </CableOptions>
</ispXCF>
"""

        xcf_template_flash = """<?xml version='1.0' encoding='utf-8' ?>
<!DOCTYPE       ispXCF  SYSTEM  "IspXCF.dtd" >
<ispXCF version="R1.2.0">
    <Comment></Comment>
    <Chain>
        <Comm>JTAG2SPI</Comm>
        <Device>
            <SelectedProg value="TRUE"/>
            <Pos>1</Pos>
            <Vendor>Lattice</Vendor>
            <Family>LIFCL</Family>
            <Name>LIFCL-40</Name>
            <Package>All</Package>
            <Bypass>
                <InstrLen>8</InstrLen>
                <InstrVal>11111111</InstrVal>
                <BScanLen>1</BScanLen>
                <BScanVal>0</BScanVal>
            </Bypass>
            <File>{bitstream_file}</File>
            <MemoryType>External SPI Flash Memory (SPI FLASH)</MemoryType>
            <Operation>Erase,Program,Verify</Operation>
            <Option>
                <SVFVendor>JTAG STANDARD</SVFVendor>
                <Usercode>0x00000000</Usercode>
                <AccessMode>Direct Programming</AccessMode>
            </Option>
            <FPGALoader>
            <CPLDDevice>
                <Device>
                    <Pos>1</Pos>
                    <Vendor>Lattice</Vendor>
                    <Family>LIFCL</Family>
                    <Name>LIFCL-40</Name>
                    <IDCode>0x010f1043</IDCode>
                    <Package>All</Package>
                    <PON>LIFCL-40</PON>
                    <Bypass>
                        <InstrLen>8</InstrLen>
                        <InstrVal>11111111</InstrVal>
                        <BScanLen>1</BScanLen>
                        <BScanVal>0</BScanVal>
                    </Bypass>
                    <MemoryType>Static Random Access Memory (SRAM)</MemoryType>
                    <Operation>Refresh Verify ID</Operation>
                    <Option>
                        <SVFVendor>JTAG STANDARD</SVFVendor>
                        <IOState>HighZ</IOState>
                        <PreloadLength>362</PreloadLength>
                        <IOVectorData>0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF</IOVectorData>
                        <AccessMode>Direct Programming</AccessMode>
                    </Option>
                </Device>
            </CPLDDevice>
            <FlashDevice>
                <Device>
                    <Pos>1</Pos>
                    <Vendor>Macronix</Vendor>
                    <Family>SPI Serial Flash</Family>
                    <Name>MX25L12833F</Name>
                    <IDCode>0x18</IDCode>
                    <Package>8-pin SOP</Package>
                    <Operation>Erase,Program,Verify</Operation>
                    <File>{bitstream_file}</File>
                    <AddressBase>0x00000000</AddressBase>
                    <EndAddress>0x000F0000</EndAddress>
                    <DeviceSize>128</DeviceSize>
                    <DataSize>1016029</DataSize>
                    <NumberOfDevices>1</NumberOfDevices>
                    <ReInitialize value="FALSE"/>
                </Device>
            </FlashDevice>
            <FPGADevice>
                <Device>
                    <Pos>1</Pos>
                    <Name></Name>
                    <File>{bitstream_file}</File>
                    <LocalChainList>
                        <LocalDevice index="-99"
                            name="Unknown"
                            file="{bitstream_file}"/>
                    </LocalChainList>
                    <Option>
                        <SVFVendor>JTAG STANDARD</SVFVendor>
                    </Option>
                </Device>
            </FPGADevice>
            </FPGALoader>
        </Device>
    </Chain>
    <ProjectOptions>
        <Program>SEQUENTIAL</Program>
        <Process>ENTIRED CHAIN</Process>
        <OperationOverride>No Override</OperationOverride>
        <StartTAP>TLR</StartTAP>
        <EndTAP>TLR</EndTAP>
        <DisableCheckBoard value="TRUE"/>
        <VerifyUsercode value="FALSE"/>
        <TCKDelay>3</TCKDelay>
    </ProjectOptions>
    <CableOptions>
        <CableName>USB2</CableName>
        <PortAdd>FTUSB-0</PortAdd>
        <USBID>Lattice ECP5 VIP Processor Board 0000 Serial FT4RXXZ5</USBID>
    </CableOptions>
</ispXCF>
"""

        if mode == "direct":
            xcf_template = xcf_template_direct
        if mode == "flash":
            xcf_template = xcf_template_flash

        return LatticeProgrammer(xcf_template)



